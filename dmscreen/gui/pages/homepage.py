from gi.repository import Gtk


class HomePage(Gtk.Box):
    spell_store = None

    def __init__(self):
        Gtk.Box.__init__(self)
        self.set_border_width(10)
        self.add(Gtk.Label(label="Page 1"))

        self.spell_store = Gtk.ListStore(int, str)
