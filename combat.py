#!/usr/bin/env python3

from math import sqrt, cos, sin, tan, acos, asin, atan2
from random import random, randint

from util import *
from char import *
#from functional import *
from team import *
from timing import *

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

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

    #timed(f'(i={i}, j={j}, mt={mt}, mb={mb})')
    srcs = front[i]
    src = srcs[j]
    target = src.target
    if(target == src):
        src.target = None
    if(target != None and alive(target)):
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
                print(f'{tij}', end='')
            timed(') won!')
            found = False
            if(len(bi) > 0):
                timed('Killed in action: ', end='')
                for bij in bi:
                    if(found):
                        timed('', end=', ')
                    found = True
                    timed(f'{bij}', end='')
            else:
                timed(f'  No casualties reported.')
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
    for ti in front:
        mt = 0
        for tij in ti:
            if(tij != None and alive(tij)):
                dm = max(0, tij.stats.INV)
                #print(f'# {tij} has INV = {dm}')
                mt = mt + dm
        totals.append(mt)
        total = total + mt
        n = n + 1

    #p = random()*total

    i = 0
    partial = random() * total
    #partial = partial * total
    for ti in front:
        j = 0
        for tij in ti:
            if(tij != None and alive(tij)):
                inv = max(0, tij.stats.INV)
                if(partial <= inv):
                    return [i, j]
                partial = partial - inv
                j = j + 1
        i = i + 1
    return [-1, -1]

def armor(dest):
    arm = clamp(dest.stats.ARM,0,20)/20.0
    return sqrt(arm*(arm+2)/3)*20

def evade(dest):
    arm = armor(dest)/20.0
    if(random() < arm/2):
        timed(f'  {dest} dodged!')
        return True
    return False

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
    d0 = clamp(s.DEX, 0, 20)
    i0 = clamp(s.INV, 0, 20)
    s0 = clamp(s.STR, 0, 20)

    p1 = .75
    x = d.ARM/20.
    a1 = 20*sqrt(x*(x+2)/3)
    #a1 = clamp(d.ARM, 0, 20)
    d1 = clamp(d.DEX, 0, 20)

    l = d0 * p0 + i0 * (1 - p0)
    r = a1 * p1 + d1 * (1 - p1)

    timed(f'DEX = {int(d0)}, INV = {int(i0)};',
            f'{p0:.2f}*{int(d0)} +',
            f'{1-p0:.2f}*{int(i0)} = {l:.1f}')
    timed(f'ARM = {int(d.ARM):2} -> {int(a1):2}, ' \
            f'DEX = {int(d1):2}; ' \
            f'{p1:.2f}*{int(a1):2} ' \
            f'+ {1-p1:.2f}*{int(d1):2} = {r:.1f}')

    p2 = random()
    p3 = p2 * (l + r)
    timed(f'  {l:.1f} vs. (random()={p2:.2f})' \
            f'*({l:.1f} + {r:.1f}) = {p3:.1f}')

    dmg = s0 * d0 * .8
    #timed(f'dmg = {str(s0)}*{str(d0)}/20 = {str(dmg)}')

    timed(f'  Damage = 16*{s0:.1f}*{d0:.1f}/20 = {dmg:.1f}')

    if(l < p3):
        dmg = 0
    s.INV = .9 * s.INV
    timed(f'    Reduced {src}\'s INV to {s.INV:.1f}')

    if(h1 <= dmg):
        die(dest)
        src.target = None
    else:
        d.HP = h1 - dmg
    return dmg


