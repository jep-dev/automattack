#!/usr/bin/env python3

from time import sleep
from combat import *
import random
import sys

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

def main():
    args = sys.argv

    seed = -1
    seeded = False
    if(len(args) == 2):
        seed = int(args[1])
        seeded = True
    if(seeded):
        random.seed(seed)

    timed(f'Seeded={seeded}, seed={seed}\n')

    G = Group
    front = G(G(Elf("Guelf"), Elf("Shelf"), Elf("Self")),
            G(Goblin("Grog"), Goblin("Flog"), Goblin("Blog")),
            G(Human("Finn"), Human("Lynn"), Human("Flynn")),
            G(Orc("Dorc"), Orc("Morc"), Orc("Porc")))
    back = G()
    last = None

    k = -1
    while(cleanup(front, back)):
        d = 0
        z = 0
        init = initiator(front, back)
        if(len(init) != 2):
            break
        i, j = init
        if(i < 0 or j < 0):
            break
        if(i >= len(front) or j >= len(front[i])):
            break

        cur = front[i][j]
        if(last == None):
            last = cur
        elif(last != cur):
            last.stats.INV = last.base_stats.INV
            timed(f'  Reset {last}\'s INV')

        pre = cur.target
        if(cur == pre):
            cur.target = None
            pre = cur.target
        if(cur.target == None or not alive(cur.target)):
            if(not retarget(i, j, front, back)):
                break
        post = cur.target
        if(evade(post)):
            timed(f'  {cur} swung, but {post} evaded')
        else:
            d = damage(cur)
        if(d > 0):
            timed(f'  {cur} hit',
                    f'{post} for {d:.1f} damage')
            if(dead(post)):
                timed(f'  {post} is dead')
        else:
            timed(f'  {cur} missed {post}')

        last = cur
        timed("")
        midsleep()

    input("\nPress <enter> to quit. ")
    return

if __name__ == "__main__":
    main()
