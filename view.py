#!/usr/bin/env python3

import sys
from time import sleep

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

class Frame(Gtk.Window):
    def run(self):
        self.win.show_all()
        Gtk.main()
    def __init__(self, t = ""):
        super().__init__(title = t)
        self.win = Gtk.Window()
        self.win.connect("destroy", Gtk.main_quit)


def main():
    Frame("Automattack").run()
    return 0

if __name__ == "__main__":
    print('Running view.py;')
    if(main() == 0):
        print('Run successful.')
        sys.exit(0)
    print('Run failed.')
    sys.exit(1)
