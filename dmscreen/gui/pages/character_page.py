import sys
from gi.repository import Gtk
from dmscreen.gui.elements.spells_sheet import SpellsSheet
from dmscreen.models.character import Character
from dmscreen.models.classes import Class


class CharacterPage(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)
        builder = Gtk.Builder()
        try:
            builder.add_from_file("dmscreen/gui/charactersheet.ui")
        except FileNotFoundError:
            print("file not found")
            sys.exit()
        box = builder.get_object("box_player_sheet")
        spells_box = builder.get_object("character_sheet_tab_spells")

        self.character = Character()
        class_ = Class()
        class_.id = 1
        self.character.classes.append(class_)
        self.character.spells.spells[0][0] = 31
        self.character.spells.spells[0][1] = 200

        SpellsSheet(spells_box, self.character)

        ab_acrobatics = builder.get_object("entry_skills_acrobatics")
        ab_acrobatics.set_text("10")
        self.add(box)
