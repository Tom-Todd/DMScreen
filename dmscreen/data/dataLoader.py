import json


def GetSpellNames(level):
    f = open('dmscreen/data/allSpells-new.json',)
    data = json.load(f)
    spells = []

    for i in data["allSpells"]:
        if i["level"] == level:
            spells.append([i["id"], i["name"]])

    f.close()
    return spells


def GetClassID(x):
    return {
        'Barbarian': 0,
        'Bard': 1,
        'Cleric': 2,
        'Druid': 3,
        'Fighter': 4,
        'Monk': 5,
        'Paladin': 6,
        'Ranger': 7,
        'Rogue': 8,
        'Sorcerer': 9,
        'Warlock': 10,
        'Wizard': 11,
    }.get(x)