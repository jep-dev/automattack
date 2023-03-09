#!/usr/bin/env python3

from combat import *
from time import sleep

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

def main():
    l = [Human("Finn"), Human("Lynn"), Human("Flynn")]
    r = [Orc("Borc"), Orc("Dorc"), Orc("Morc")]

    k = -1
    while(True):
        init = initiator(l, r)
        if(len(init) != 2):
            break
        d = 0
        z = 0
        section, item = init
        if(section == 0):
            pre = item.target
            if(pre == None or dead(pre)):
                if(not retarget(item, r)):
                    break
            d = damage(item)
            if(d > 0):
                print(f'{str(item)} hit',
                        f'{str(r[z])} for {str(d)}')
                if(dead(r[z])):
                    print(f'{str(r[z])} is dead')
            else:
                print(f'{str(item)} missed {str(r[z])}')
        elif(section == 1):
            pre = item.target
            if(pre == None or dead(pre)):
                if(not retarget(item, r)):
                    break
            d = damage(item)
            if(d > 0):
                print(f'{str(item)} hit',
                        f'{str(l[z])} for {str(d)}')
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
