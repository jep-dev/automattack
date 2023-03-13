#!/usr/bin/env python3

from combat import *
from time import sleep

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

def main():
    front = [[Human("Finn"), Human("Lynn"), Human("Flynn")],
            [Orc("Dorc"), Orc("Morc"), Orc("Porc")],
            [Elf("Guelf"), Elf("Shelf"), Elf("Self")],
    ]
    back = [[], [], []]
    last = None

    k = -1
    while(True):
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

        item = front[i][j]
        if(last == None):
            last = item
        elif(last != item):
            last.stats.INV = last.base_stats.INV
            print(f'  Reset {last}\'s INV')

        pre = item.target
        if(item == pre):
            item.target = None
            pre = item.target
        if(item.target == None or not alive(item.target)):
            if(not retarget(i, j, front, back)):
                break
        post = item.target
        d = damage(item)
        if(d > 0):
            print(f'  {item} hit',
                    f'{post} for {d:.2f} damage')
            if(dead(post)):
                print(f'  {post} is dead')
        else:
            print(f'  {item} missed {post}')
        if(not cleanup(front, back)):
            print(f'\nCleanup returned false.')
            break

        sleep(2)
        print("")

    input("\nPress <enter> to quit. ")
    return

if __name__ == "__main__":
    main()
