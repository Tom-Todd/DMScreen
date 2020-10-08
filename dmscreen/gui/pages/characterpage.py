import sys
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import GLib, Gio, Gtk

class CharacterPage(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)
        self.set_border_width(10)
        grid = AbilityScoreGrid(True)
        self.add(grid)


class AbilityScoreGrid(Gtk.Grid):
    def __init__(self, vertical):
        Gtk.Grid.__init__(self)

        ab_str = AbilityScoreBox("STR", 5)
        ab_dex = AbilityScoreBox("DEX", 5)
        ab_con = AbilityScoreBox("CON", 5)
        ab_int = AbilityScoreBox("INT", 5)
        ab_wis = AbilityScoreBox("WIS", 5)
        ab_cha = AbilityScoreBox("CHA", 5)

        orientation =  Gtk.PositionType.BOTTOM if vertical else Gtk.PositionType.RIGHT

        self.add(ab_str)
        self.attach_next_to(ab_con, ab_str, orientation,1,1)
        self.attach_next_to(ab_dex, ab_con, orientation,1,1)
        self.attach_next_to(ab_int, ab_dex, orientation,1,1)
        self.attach_next_to(ab_wis, ab_int, orientation,1,1)
        self.attach_next_to(ab_cha, ab_wis, orientation,1,1)

class AbilityScoreBox(Gtk.Frame):
    def __init__(self, label_text, score):
        Gtk.Frame.__init__(self)

        label = Gtk.Label(label=label_text)
        label.set_hexpand(False)
        box = Gtk.Box()
        entry = Gtk.Entry()
        entry.set_max_width_chars(2)
        entry.set_placeholder_text("10")
        entry.set_text("10")
        entry.set_width_chars(2)

        grid = Gtk.Grid()
        grid.add(label)
        grid.attach_next_to(entry, label, Gtk.PositionType.BOTTOM,1,1)
        self.add(grid)
        self.set_border_width(2)
        self.set_hexpand(False)
