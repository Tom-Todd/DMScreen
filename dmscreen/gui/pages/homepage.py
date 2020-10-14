from gi.repository import Gtk
from dmscreen.data.jsonconvert import GetSpellNames


class HomePage(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)
        self.set_border_width(10)
        self.add(Gtk.Label(label="Page 1"))

        spell_store = Gtk.ListStore(int, str)

        for data in GetSpellNames():
            spell_store.append(data)


        combo = Gtk.ComboBox.new_with_model(spell_store)
        renderer_text = Gtk.CellRendererText()
        combo.pack_start(renderer_text, True)
        combo.add_attribute(renderer_text, "text", 1)
        combo.connect("changed", self.on_skills_combo_changed)

        grid = Gtk.Grid()
        grid.add(combo)
        self.pack_start(grid, False, False, True)

    def on_skills_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            id = model[tree_iter][0]
            print(id)
