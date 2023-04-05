#!/usr/bin/env python3

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

from util import *
import math
import sys

def ltransform(f, x, *y):
    t = type(x)
    if(issubclass(t, list)):
        return [f(xi, *y) for xi in x]
    elif(issubclass(t, tuple)):
        return (f(xi, *y) for xi in x)
    return None

def rtransform(f, x, y, *z):
    t = type(y)
    if(issubclass(t, list)):
        return [f(x, yi, *z) for yi in y]
    elif(issubclass(t, tuple)):
        return (f(x, yi, *z) for yi in y)
    return None

def ftransform(f, *x):
    t = type(f)
    if(issubclass(t, list)):
        return [fi(*x) for fi in f]
    elif(issubclass(t, tuple)):
        return (fi(*x) for fi in f)
    return None

def lbind(f, *y, **z):
    return lambda x : f(*y, x, **z)

def rbind(f, *y, **z):
    return lambda x : f(x, *y, **z)

def fnot(f, *y, **z):
    return lambda *x : not f(*x, *y, **z)

def ffilter(f, x, *y, **z):
    t = type(x)
    if(not issubclass(t, (list, tuple))):
        return [None, None]
    out = [[], []]
    for xi in x:
        out[f(xi, *y, **z)].append(xi)
    if(issubclass(t, list)):
        return out
    if(issubclass(t, tuple)):
        return [(u for u in out[0]), (v for v in out[1])]
    return [None, None]

def finclude(f, x, *y, **z):
    return ffilter(f, x, *y, **z)[0]

def fexclude(f, x, *y, **z):
    return ffilter(f, x, *y, **z)[1]

def test_functional():
    f = lambda x,*y,**z: math.isfinite(x)
    g = fnot(f)
    x0 = math.nan
    x1 = math.inf
    x2 = 0.0
    xn = [-x0, -x1, -x2, x2, x1, x0]
    lx = len(xn)
    print(f'X[{lx}] = {xn}')
    for xi in xn:
        assert f(xi) == (not g(xi))

    u,v = ffilter(f, xn)
    for uj in u:
        assert g(uj)
    lu = len(u)
    print(f'U[{lu}] = {u}')

    for vk in v:
        assert f(vk)
    lv = len(v)
    print(f'V[{lv}] = {v}')
    assert lu + lv == lx
    return True

if(__name__ == "__main__"):
    print('Testing functional.py;')
    if(test_functional()):
        print('Test passed.')
        sys.exit(0)
    print('Test failed.')
    sys.exit(1)
