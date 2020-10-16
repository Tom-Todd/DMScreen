#!/usr/bin/env python3
import os
import sys

from setuptools import setup

from dmscreen import __version__ as VERSION

if sys.version_info < (3, 6):
    sys.exit('Python 3.6 is required to run DMScreen')

for directory, _, filenames in os.walk(u'share'):
    dest = directory[6:]
    if filenames:
        files = []
        for filename in filenames:
            filename = os.path.join(directory, filename)
            files.append(filename)

setup(
    name='DMScreen',
    version=VERSION,
    author='Tom Todd',
    author_email='thomas.m.a.todd@gmail.com',
    packages=[
        'dmscreen',
        'dmscreen.gui',
        'dmscreen.gui.pages',
        'dmscreen.util',
    ],
    scripts=['bin/dmscreen.py'],
    description='D&D 5e DM Screen Application',
    long_description="""An application for keeping track of and generating
     information for dungeon masters in D&D fifth edition.""",
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python',
        'Operating System :: Linux',
        'Topic :: Games/Entertainment'
    ],
)
