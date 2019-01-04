import os
import qrcode
import qrcode.image.svg
import json

factory = qrcode.image.svg.SvgPathImage

index = 1

with open('CTOK000001.json', 'r') as data:
    string_data = data.read()

json_data = json.loads(string_data)
for x in json_data:
    save(x + ":", json_data[x])
    pubkey = qrcode.make(x, image_factory = factory)
    prvkey = qrcode.make(json_data[x], image_factory = factory)
    if not os.path.exists("folder{}".format(index)):
        os.makedirs("folder{}".format(index))
        pubkey.save("pubkey{}.svg".format(index))
        prvkey.save("prvkey{}.svg".format(index))
        os.system("mv pubkey{}.svg folder{}".format(index, index))
        os.system("mv prvkey{}.svg folder{}".format(index, index))        
    index += 1
