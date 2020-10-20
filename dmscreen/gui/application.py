# pylint: disable=wrong-import-position
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gio, Gtk  # noqa: E402

from dmscreen.gui.pages.character_page import CharacterPage  # noqa: E402
from dmscreen.gui.pages.home_page import HomePage  # noqa: E402
from dmscreen.data.jsonconvert import ParseData  # noqa: E402

UI_STRING = """
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <menu id="menubar">
    <submenu>
      <attribute name="label">File</attribute>
      <section>
        <item>
          <attribute name="label">New</attribute>
          <attribute name="action">app.new</attribute>
        </item>
      </section>
    </submenu>
  </menu>
</interface>
"""


class AppWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, title="DM Screen", application=app)
        self.set_default_size(600, 600)
        self.set_border_width(3)
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        self.page1 = HomePage()
        self.notebook.append_page(self.page1, Gtk.Label(label="Home"))

        self.page2 = CharacterPage()
        self.notebook.append_page(self.page2, Gtk.Label(label="Characters"))


class Application(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)
        new_action = Gio.SimpleAction.new("new", None)
        new_action.connect("activate", self.new_callback)
        self.add_action(new_action)

    def new_callback(self, action, parameter):
        print("You clicked \"New\"")

    def do_activate(self):
        win = AppWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

        ParseData()

        builder = Gtk.Builder()
        try:
            builder.add_from_file("dmscreen/gui/menubar.ui")
        except FileNotFoundError:
            print("file not found")
            sys.exit()

        self.set_menubar(builder.get_object("menubar"))
