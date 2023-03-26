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
    sprite.position = 10,10
    renderer.render(sprite)
    sprite.position = 100,10
    return [RES, win, fac, sprite]

def run(win):
    evs = sdl2.ext.get_events()
    for ev in evs:
        if ev.type == sdl2.SDL_QUIT:
            return False
    win.refresh()
    return True

def stop(win):
    win.close()
    sdl2.ext.quit()

def main():
    args = sys.argv
    res, win, fac, spr = init()
    while(run(win)):
        continue
    stop(win)

if __name__ == "__main__":
    main()
