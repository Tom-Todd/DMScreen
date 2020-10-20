import json


def get_spell_names(class_id, level_id):
    f = open('dmscreen/data/allSpells-new.json',)
    data = json.load(f)
    spells = []

    for i in data["allSpells"]:
        if i["level"] == level_id and (class_id == -1 or class_id in i["classes"]):
            spells.append([i["id"], i["name"]])

    f.close()
    return spells


def get_class_id(x):
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
