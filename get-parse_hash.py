import siaskynet as skynet
import re

client = skynet.SkynetClient()
skylink = "AAAxbSSDj4GcPcCcWGk0mhqxbHY-Btkuq8FGixOtKBzuyA" # HERE'S OUR SKYLINK

client.download_file("./push", skylink)

with open("push","r") as file:
    for line in file:
        if re.search("hash link", line):
            print(line[line.find('link ')+5:]) # HERE'S OUR IMAGE_HASH
