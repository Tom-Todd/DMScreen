import sys
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import GLib, Gio, Gtk

class HomePage(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)
        self.set_border_width(10)
        self.add(Gtk.Label(label="Page 1"))
