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
    s.HP = 0.0
    s.INV = 0.0
    s.INT = 0.0
    c.target = None

def dead(c):
    s = c.stats
    return (s.HP <= 0) or (s.INT <= 0)
def alive(c):
    return not dead(c)

def retarget(i, j, front, back):
    mt = len(front)
    mb = len(back)
    m = max(mt, mb)
    dm = max(m-mt, m-mb)
    for k in range(dm):
        if(mt < mb):
            front.append([])
        elif(mt > mb):
            back.append([])

    life = []
    death = []

    print(f'(i={i}, j={j}, mt={mt}, mb={mb})')
    srcs = front[i]
    src = srcs[j]
    target = src.target
    if(target == src):
        src.target = None
    if(target != None and alive(target)):
        if(alive(target)):
            return True

    for k in range(m):
        if(i == k):
            continue
        fk = front[k]
        bk = back[k]
        for l in range(len(fk)):
            fkl = fk[l]
            if(fkl == None):
                continue
            if(alive(fkl)):
                life.append([k,l])
                continue
            death.append([k,l])

    nlife = len(life)
    if(nlife < 1):
        return False
    rng = randint(0, nlife-1)
    k,l = life[rng]
    src.target = front[k][l]
    return True


def cleanup(front, back):
    m = len(front)
    n = len(back)

    while(m > n):
        back.append([])
        n = n + 1
    while(n > m):
        front.append([])
        m = m + 1
    if(m < 2):
        return False

    i = 0
    while(i < m):
        ti = front[i]
        bi = back[i]
        nt = len(ti)
        nb = len(bi)
        j = 0
        while(j < nt):
            tij = ti[j]
            if(tij == None):
                ti.pop(j)
                nt = nt - 1
            elif(alive(tij)):
                j = j + 1
                continue
            bi.append(ti.pop(j))
            nb = nb + 1
            nt = nt - 1
        j = 0
        while(j < nb):
            bij = bi[j]
            if(bij == None):
                bi.pop(j)
                nb = nb - 1
            elif(alive(bij)):
                ti.append(bi.pop(j))
                nt = nt + 1
                nb = nb - 1
                continue
            j = j + 1
        i = i + 1
    i = 0
    while(i < m):
        ti = front[i]
        bi = back[i]
        out = True
        for k in range(len(ti)):
            if(not retarget(i, k, front, back)):
                out = False
        if(not out):
            found = False
            print(f'\nTeam {i} (', end='')
            for tij in ti:
                if(found):
                    print('', end=', ')
                found = True
                print(f'{str(tij)}', end='')
            print(') won!')
            found = False
            if(len(bi) > 0):
                print('Killed in action: ', end='')
                for bij in bi:
                    if(found):
                        print('', end=', ')
                    found = True
                    print(f'{str(bij)}', end='')
            else:
                print(f'  No casualties reported.')
            return False
        i = i + 1
    return True

def initiator(front, back):
    #cleanup(lhs, rhs)
    #if(not cleanup(lhs, rhs)):
    #    return ()

    n = 0     # Number of front
    total = 0 # Sum of INV
    totals = []
    for t in front:
        mt = 0
        for ti in t:
            if(ti != None and alive(ti)):
                mt = mt + max(0, ti.stats.INV)
        totals.append(mt)
        total = total + mt
        n = n + 1

    p = random() * total

    i = 0
    partial = 0
    for t in front:
        j = 0
        partial = totals[i]
        for ti in t:
            if(ti != None and alive(ti)):
                inv = max(0, ti.stats.INV)
                partial = partial - inv
                if(partial <= 0):
                    return [i, j]
                j = j + 1
        i = i + 1
    return [-1, -1]

def damage(src):
    s = src.stats
    dest = src.target
    d = dest.stats

    h0 = s.HP
    if(h0 <= 0):
        return 0
    h1 = d.HP
    if(h1 <= 0):
        return 0

    p0 = .6
    d0 = clamp(s.DEX)
    i0 = clamp(s.INV)
    s0 = clamp(s.STR)

    p1 = .75
    x = d.ARM/20.
    a1 = 20*sqrt(x*(x+2)/3)
    #a1 = clamp(d.ARM)
    d1 = clamp(d.DEX)

    l = d0 * p0 + i0 * (1 - p0)
    r = a1 * p1 + d1 * (1 - p1)

    print(f'DEX = {d0:.2f}, INV = {i0:.2f};',
            f'{p0}*DEX + {1-p0}*INV = {l:.2f}')
    print(f'ARM = {x*20} -> {a1:.2f}, DEX = {d1:.2f}; ' \
            f'  {p1:.2f} * {a1:.2f} ' \
            f'+ {1-p1:.2f} * {d1:.2f} = {r:.2f}')

    p2 = random()
    p3 = p2 * (l + r)
    print(f'  {l:.2f} vs. (random()={p2:.2%})',
            f'* ({l:.2f}+{r:.2f}) = {p3:.2f}')

    #dmg = .25 * s0 * d0
    dmg = s0 * d0 / 20.0
    #print(f'dmg = {str(s0)}*{str(d0)}/20 = {str(dmg)}')

    print(f'  Damage = {s0:.2f}*{d0:.2f}/20 = {dmg:.2f}')

    if(l < p2):
        s.INV = src.base_stats.INV
        print(f'    Reset {src}\'s INV to {s.INV:.2f}')
        return 0
    else:
        s.INV = .9 * s.INV
        print(f'    Reduced {src}\'s INV to {s.INV:.2f}')

    if(h1 <= dmg):
        die(dest)
        src.target = None
    else:
        d.HP = h1 - dmg
    return dmg


