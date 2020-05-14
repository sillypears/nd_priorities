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
        id = 0
        name = e.tag
        priority = 0
        e_type = 0
        sprite = ""
        for a in e.attrib:
            if a == "id":
                id = int(e.attrib[a])
            if a == "type":
                e_type = int(e.attrib[a])
        for child in e:
            if child.tag == "stats":
                if "priority" in child.attrib:
                    priority = int(child.attrib["priority"])
            if child.tag == "spritesheet":
                sprite = child.text
        enemies[str(id)] = {'type': e_type, 'name': name, 'priority': priority, 'sprite': sprite}
    o_enemies = OrderedDict(sorted(enemies.items(), key = lambda x: getitem(x[1], 'priority')))
    with open("necrodancer.json", 'w') as w:
        w.write(json.dumps(o_enemies))
    return 0

if __name__ == "__main__":
    sys.exit(main())
