import os,sys
import xml.etree.ElementTree as ET
from collections import OrderedDict
from operator import getitem
import json

XMLF = "necrodancer.xml"

def main():
    root = ET.parse(XMLF).getroot()
    enemies = {}
    for e in root[1]:
        name = e.tag
        priority = 0
        e_type = 0
        sprite = ""
        s_x = 0
        s_y = 0
        for a in e.attrib:
            if a == "type":
                e_type = int(e.attrib[a])
        for child in e:
            if child.tag == "stats":
                if "priority" in child.attrib:
                    priority = int(child.attrib["priority"])
            if child.tag == "spritesheet":
                sprite = child.text
                s_x = child.attrib["frameW"]
                s_y = child.attrib["frameH"]
        if priority > 0:
            enemies[sprite] = {'type': e_type, 'name': name, 'priority': priority, 'sprite': sprite, 'frameW': s_x, 'frameH': s_y}
    enemies = OrderedDict(sorted(enemies.items(), key = lambda x: getitem(x[1], 'priority')))
    print(enemies)
    new_enemies = []
    
    for e in enemies:
        new_enemies.append(enemies[e])
    with open("necrodancer.json", 'w') as w:
        w.write(json.dumps(new_enemies))
    return 0

if __name__ == "__main__":
    sys.exit(main())
