#!/usr/bin/env python3
import asyncio
from typing import AsyncIterable

from yapapi import Golem, Task, WorkContext
from yapapi.log import enable_default_logger
from yapapi.payload import vm

import siaskynet as skynet
import re
import aiofiles

async def worker(context: WorkContext, tasks: AsyncIterable[Task]):
    async for task in tasks:
        script = context.new_script()

        # upload & run the provider.sh script
        future_result = script.run("/bin/sh", "-c", 'echo "Hello World!"')

        yield script

        task.accept_result(result=await future_result)

async def get_hash():
    client = skynet.SkynetClient()
    skylink = "AAAxbSSDj4GcPcCcWGk0mhqxbHY-Btkuq8FGixOtKBzuyA" # HERE'S OUR SKYLINK
    client.download_file("./push", skylink)
    
    async with aiofiles.open('push', mode='r') as f:
        async for line in f:
            if re.search("hash link", line):
                return str(line[line.find('link ')+5:].strip()) # HERE'S OUR IMAGE_HASH

    # IF NOT FOUND, EXIT
    print("Could not parse hash from push file")
    exit()

async def main():
    hash = await get_hash()
    
    package = await vm.repo( 
        image_hash=hash,
    )

    tasks = [Task(data=None)]

    async with Golem(budget=1.0, subnet_tag="devnet-beta") as golem:
        async for completed in golem.execute_tasks(worker, tasks, payload=package):
            # print out the console output
            print(completed.result.stdout)


if __name__ == "__main__":
    enable_default_logger(log_file="out.log")

    loop = asyncio.get_event_loop()
    task = loop.create_task(main())
    loop.run_until_complete(task)
