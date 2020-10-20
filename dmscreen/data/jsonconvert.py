import json
from dmscreen.data.dataLoader import get_class_id


def ParseData():
    f = open('dmscreen/data/allSpells.json',)

    data = json.load(f)

    id_ = 0
    for i in data["allSpells"]:
        classes = []
        for s in i["classes"].split(", "):
            classes.append(get_class_id(s))

        i["classes"] = classes
        i["id"] = id_
        id_ += 1

    f2 = open('dmscreen/data/allSpells-new.json', 'w')
    json.dump(data, f2, indent=4)
    f.close()
