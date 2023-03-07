#!/usr/bin/env python3

from combat import *
from time import sleep

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

def main():
    l = [Human("Finn")]
    r = [Elf("Shelf"), Orc("Dorc")]

    k = -1
    while(True):
        init = initiator(l, r)
        if(len(init) != 2):
            break
        d = 0
        z = 0
        side, item = init
        if(side == 0):
            if(item.target == None or dead(item.target)):
                z = randint(0, len(r)-1)
                item.target = r[z]
                d = damage(item, r[z])
            if(d > 0):
                print(f'{str(item)} hit',
                        f'{str(r[z])} for {str(d)}')
                if(dead(r[z])):
                    print(f'{str(r[z])} is dead')
            else:
                print(f'{str(item)} missed {str(r[z])}')
        elif(side == 1):
            if(item.target == None or dead(item.target)):
                z = randint(0, len(l)-1)
                item.target = l[z]
            d = damage(item, item.target)
            if(d > 0):
                print(f'{str(item)} hit {str(l[z])} ({str(d)})')
                if(dead(l[z])):
                    print(f'{str(l[z])} is dead')
            else:
                print(f'{str(item)} missed {str(l[z])}')
        else:
            break
        cleanup(l, r)
        sleep(1)

    print(f'Done')

    return

if __name__ == "__main__":
    main()
