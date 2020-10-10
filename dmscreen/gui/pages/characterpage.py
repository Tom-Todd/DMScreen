import gi
import sys

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class CharacterPage(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)
        builder = Gtk.Builder()
        try:
            builder.add_from_file("dmscreen/gui/charactersheet.ui")
        except:
            print("file not found")
            sys.exit()
        box = builder.get_object("box_player_sheet")
        ab_acrobatics = builder.get_object("entry_skills_acrobatics")
        ab_acrobatics.set_text("10")

        self.add(box)