import siaskynet as skynet
import re
import aiofiles

async def get_hash():
    client = skynet.SkynetClient()
    skylink = "AAAxbSSDj4GcPcCcWGk0mhqxbHY-Btkuq8FGixOtKBzuyA" # HERE'S OUR SKYLINK
    client.download_file("./push", skylink)
    
    async with aiofiles.open('push', mode='r') as f:
        async for line in f:
            if re.search("hash link", line):
                return str(line[line.find('link ')+5:][:-1]) # HERE'S OUR IMAGE_HASH

    # IF NOT FOUND, EXIT
    print("Could not parse hash from push file")
    exit()

print(await get_hash) # PRINTS OUR HASH
