from gi.repository import Gtk
from dmscreen.data.data_loader import get_spell_names_for_class


class SpellsSheet:
    def __init__(self, spells_box, character):
        self.spell_store_cantrips = Gtk.ListStore(int, str)
        self.spell_store_level_one = Gtk.ListStore(int, str)
        self.spell_store_level_two = Gtk.ListStore(int, str)
        self.character = character

        for class_ in character.classes:
            spell_names = get_spell_names_for_class(class_.id)
            for data in spell_names[0]:
                self.spell_store_cantrips.append(data)
            for data in spell_names[1]:
                self.spell_store_level_one.append(data)
            for data in spell_names[2]:
                self.spell_store_level_two.append(data)

        label_cantrips = Gtk.Label(label="Cantrips (Level 0)")
        label_spells1 = Gtk.Label(label="Level 1")
        label_spells2 = Gtk.Label(label="Level 2")

        grid = Gtk.Grid()
        grid.add(label_cantrips)
        grid.attach_next_to(label_spells1, label_cantrips, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(label_spells2, label_spells1, Gtk.PositionType.RIGHT, 1, 1)

        for i in range(1, 6):
            grid.attach(self.skills_combo(self.spell_store_cantrips, 0, i-1), 0, i, 1, 1)
            grid.attach(self.skills_combo(self.spell_store_level_one, 1, i-1), 1, i, 1, 1)
            grid.attach(self.skills_combo(self.spell_store_level_two, 2, i-1), 2, i, 1, 1)

        spells_box.pack_start(grid, False, False, True)

    def skills_combo(self, spell_store, level_id, combo_id):
        combo = Gtk.ComboBox.new_with_model(spell_store)
        renderer_text = Gtk.CellRendererText()
        combo.pack_start(renderer_text, True)
        combo.add_attribute(renderer_text, "text", 1)
        combo.connect("changed", self.on_skills_combo_changed, level_id, combo_id)
        for i in range(len(spell_store)):
            row = spell_store[i]
            if row[0] == self.character.spells.spells[level_id][combo_id]:
                combo.set_active(i)
        return combo

    def on_skills_combo_changed(self, combo, level_id, combo_id):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            id_ = model[tree_iter][0]
            self.character.spells.spells[level_id][combo_id] = id_
