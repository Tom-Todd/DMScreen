
"""Main entry point for DMScreen"""
import sys
import os
from os.path import realpath, dirname, normpath

LAUNCH_PATH = dirname(realpath(__file__))

if os.path.isdir(os.path.join(LAUNCH_PATH, "../dmscreen")):
    SOURCE_PATH = normpath(os.path.join(LAUNCH_PATH, '..'))
    sys.path.insert(0, SOURCE_PATH)
else:
    sys.path.insert(0, os.path.normpath(os.path.join(LAUNCH_PATH, "../lib/dmscreen")))


from dmscreen.gui.application import Application   # pylint: disable=no-name-in-module noqa:E402

app = Application()
sys.exit(app.run(sys.argv))
