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
        i, j = initiator(l, r)
        if(i == -1):
            k = j
            break
        if(i == 0):
            z = randint(0, len(r)-1)
            d = damage(l[j], r[z])
            if(d > 0):
                print(f'{str(l[j])} hit {str(r[z])} ({str(d)})')
            else:
                print(f'{str(l[j])} missed {str(r[d])}')
            if(dead(r[z])):
                print(f'{str(r[z])} is dead')
        elif(i == 1):
            z = randint(0, len(l)-1)
            d = damage(r[j], l[z])
            if(d > 0):
                print(f'{str(r[j])} hit {str(l[z])} ({str(d)})')
            else:
                print(f'{str(r[j])} missed {str(l[z])}')
            if(dead(l[z])):
                print(f'{str(l[z])} is dead')
        else:
            break
        sleep(1)
    print(f'Done (k = {k})')

    return

if __name__ == "__main__":
    main()
