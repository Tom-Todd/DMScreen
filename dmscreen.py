
"""Main entry point for DMScreen"""
import sys
from dmscreen.gui.application import Application   # pylint: disable=no-name-in-module

app = Application()
sys.exit(app.run(sys.argv))
