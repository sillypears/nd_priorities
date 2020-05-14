from PIL import Image
import os
import json

with open('necrodancer.json') as f:
    for e in json.loads(f.read()):
        img = Image.open(e['sprite'])
        crop = img.crop((0, 0, int(e['frameW']), int(e['frameH'])))
        crop.save(e['sprite'])