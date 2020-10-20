import sys
from gi.repository import Gtk
from dmscreen.data.dataLoader import GetSpellNames


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
        self.spell_store_cantrips = Gtk.ListStore(int, str)
        self.spell_store_level_one = Gtk.ListStore(int, str)

        for data in GetSpellNames(0):
            self.spell_store_cantrips.append(data)

        for data in GetSpellNames(1):
            self.spell_store_level_one.append(data)

        label_cantrips = Gtk.Label(label="Cantrips (Level 0)")
        label_spells1 = Gtk.Label(label="Level 1")

        grid = Gtk.Grid()
        grid.add(label_cantrips)
        grid.attach_next_to(label_spells1, label_cantrips, Gtk.PositionType.RIGHT, 1, 1)

        for i in range(1, 6):
            grid.attach(self.skills_combo(self.spell_store_cantrips), 0, i, 1, 1)
            grid.attach(self.skills_combo(self.spell_store_level_one), 1, i, 1, 1)

        spells_box.pack_start(grid, False, False, True)
        ab_acrobatics = builder.get_object("entry_skills_acrobatics")
        ab_acrobatics.set_text("10")

        self.add(box)

    def skills_combo(self, spell_store):
        combo = Gtk.ComboBox.new_with_model(spell_store)
        renderer_text = Gtk.CellRendererText()
        combo.pack_start(renderer_text, True)
        combo.add_attribute(renderer_text, "text", 1)
        combo.connect("changed", self.on_skills_combo_changed)
        return combo

    def on_skills_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            id_ = model[tree_iter][0]
            print(id_)
