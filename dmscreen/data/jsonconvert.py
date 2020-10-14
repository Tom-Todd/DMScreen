import json


def ParseData():
    f = open('dmscreen/data/allSpells.json',)

    data = json.load(f)

    id = 0
    for i in data["allSpells"]:
        classes = []
        for s in i["classes"].split(", "):
            classes.append(GetClassID(s))

        i["classes"] = classes
        i["id"] = id
        id+=1

    f2 = open('dmscreen/data/allSpells-new.json', 'w')
    json.dump(data, f2, indent=4)
    f.close()


def GetClassID(x):
    return {
        'Barbarian' : 0,
        'Bard' : 1,
        'Cleric' : 2,
        'Druid' : 3,
        'Fighter' : 4,
        'Monk' : 5,
        'Paladin' : 6,
        'Ranger' : 7,
        'Rogue' : 8,
        'Sorcerer' : 9,
        'Warlock' : 10,
        'Wizard' : 11,
    }.get(x)
