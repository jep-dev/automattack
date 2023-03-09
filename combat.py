#!/usr/bin/env python3

from math import sqrt
from random import random, randint

from util import *
from char import *

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

def die(c):
    s = c.stats
    s.health = 0.0
    s.initiative = 0.0
    s.intelligence = 0.0
    s.strength = 0.0
    c.target = None

def dead(c):
    s = c.stats
    return (s.health <= 0) or (s.intelligence <= 0)
def alive(c):
    return not dead(c)

def retarget(src, dest):
    n = 0
    live = []
    target = src.target
    if(target != None):
        if(alive(target)):
            return True
    for d in dest:
        if(d != None and alive(d)):
            live.append(d)
            n = n + 1

    if(n == 0):
        src.target = None
        return False
    else:
        i = randint(0, n-1)
        d = dest[i]
        src.target = d
        return True

def cleanup(lhs, rhs):
    out = True
    i = 0
    while(i < len(lhs)):
        l = lhs[i]
        if((l == None) or dead(l)):
            lhs.pop(i)
            continue
        if(not retarget(l, rhs)):
            out = False
        i = i + 1
    j = 0
    while(j < len(rhs)):
        r = rhs[j]
        if((r == None) or dead(r)):
            rhs.pop(j)
            continue
        if(not retarget(r, lhs)):
            out = False
        j = j+1
    return out


def initiator(lhs, rhs):
    #cleanup(lhs, rhs)
    #if(not cleanup(lhs, rhs)):
    #    return ()

    m = 0
    for x in lhs:
        if(alive(x)):
            m = m + max(0, x.stats.initiative)

    n = 0
    for y in rhs:
        if(alive(y)):
            n = n + max(0, y.stats.initiative)

    p = random() * (m + n)

    for x in lhs:
        if(dead(x)):
            pass
        k = max(0, x.stats.initiative)
        p = p - k
        if(p <= 0):
            return (0, x)

    for y in rhs:
        if(dead(y)):
            pass
        k = max(0, y.stats.initiative)
        p = p - k
        if(p <= 0):
            return (1, y)

    return ()



def damage(src):
    s = src.stats
    dest = src.target
    d = dest.stats

    h0 = s.health
    if(h0 <= 0):
        return 0
    h1 = d.health
    if(h1 <= 0):
        return 0

    p0 = .6
    d0 = clamp(s.dexterity)
    i0 = clamp(s.initiative)
    s0 = clamp(s.strength)

    p1 = .75
    x = d.armor/20.
    a1 = 20*sqrt(x*(x+2)/3)
    #a1 = clamp(d.armor)
    d1 = clamp(d.dexterity)

    l = d0 * p0 + i0 * (1 - p0)
    r = a1 * p1 + d1 * (1 - p1)

    print(f'DEX = {d0:.2f}, INV = {i0:.2f},',
            f'{p0}*DEX + {1-p0}*INV = {l:.2f}')
    print(f'ARM = {x*20} -> {a1:.2f}, DEX = {d1:.2f}')
    print(f'  {p1:.2f}*{a1:.2f}',
        f'{1-p1:.2f}*{d1:.2f} = {r:.2f}')

    p2 = random()
    p3 = p2 * (l + r)
    print(f'  {l:.2f} vs. (random()={p2:.2%})',
            f'* ({l:.2f}+{r:.2f}) = {p3:.2f}')

    #dmg = .25 * s0 * d0
    dmg = s0 * d0 / 20.0
    #print(f'dmg = {str(s0)}*{str(d0)}/20 = {str(dmg)}')

    print(f'  dmg = {s0:.2f}*{d0:.2f}/20 = {dmg:.2f}')

    if(l < p2):
        s.initiative = src.base_stats.initiative
        print(f'    Reset {src}\'s initiative')
        return 0
    else:
        s.initiative = .9 * s.initiative
        print(f'    Reduced {src}\'s INV to {s.initiative:.2f}')

    if(h1 <= dmg):
        die(dest)
        src.target = None
    else:
        d.health = h1 - dmg
    return dmg


