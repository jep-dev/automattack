#!/usr/bin/env python3

import sys
import sdl2.ext
from time import sleep

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"


def init():
    sdl2.ext.init()
    RES = sdl2.ext.Resources(__file__, "share")
    win = sdl2.ext.Window("Title", size=(640,480))
    win.show()
    fac = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    sprite = fac.from_image(RES.get_path("test.png"))
    renderer = fac.create_sprite_render_system(win)
    sprite.position = 10,20
    renderer.render(sprite)
    sprite.position = 55,10
    return [RES, win, fac, sprite]

def run(win):
    processor = sdl2.ext.TestEventProcessor()
    processor.run(win)

def main():
    args = sys.argv
    res, win, fac, spr = init()
    run(win)
    sdl2.ext.quit()

if __name__ == "__main__":
    main()
