#!/usr/bin/env python3

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

import math
import sys

from util import *

def ftransform(f, *x, **y):
    t = type(f)
    if(issubclass(t, list)):
        return [fi(*x, **y) for fi in f]
    elif(issubclass(t, tuple)):
        return (fi(*x, **y) for fi in f)
    return None

def ltransform(f, x, *y, **z):
    t = type(x)
    if(issubclass(t, list)):
        return [f(xi, *y, **z) for xi in x]
    elif(issubclass(t, tuple)):
        return (f(xi, *y, **z) for xi in x)
    return None

def rtransform(f, w, x, *y, **z):
    t = type(y)
    if(issubclass(t, list)):
        return [f(w, xi, *y, **z) for xi in x]
    elif(issubclass(t, tuple)):
        return (f(w, xi, *y, **z) for xi in x)
    return None

def lbind(f, *y, **z):
    return lambda x : f(*y, x, **z)

def rbind(f, *y, **z):
    return lambda x : f(x, *y, **z)

def fnot(f, *y, **z):
    return lambda *x : not f(*x, *y, **z)

def f_or(f, g):
    return lambda x : f(x) or g(x)
def fxor(f, g):
    return lambda x : bool(f(x)) ^ bool(g(x))
def fand(f, g):
    return lambda x : f(x) and g(x)

def fcompose(f, g):
    return lambda x : f(g(x))

def fcompare(f, g):
    return lambda *y, **z : compare(f(*y, **z), g(*y, **z))

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
    return ffilter(f, x, *y, **z)[1]

def fexclude(f, x, *y, **z):
    return ffilter(f, x, *y, **z)[0]

def test_functional():
    m = 12
    u0 = [*range(0, 12)]
    t0 = [*range(0, 12, 3)]
    t1 = [*range(1, 12, 3)]
    t2 = [*range(2, 12, 3)]
    y = lambda l,r : lambda i : ((i%l+l)%l == r)

    even = y(2,0)
    odd = fnot(even)
    for i in u0:
        assert odd(i) == (not even(i))
    alt = [bool(i&1) for i in u0]
    assert ltransform(odd, u0) == alt
    alt = [not (i&1) for i in u0]
    assert ltransform(even, u0) == alt

    v0,v1 = ffilter(odd, u0)
    assert v0 == [*range(0, 12, 2)]
    assert v1 == [*range(1, 12, 2)]
    return True


if(__name__ == "__main__"):
    print('Testing functional.py;')
    if(test_functional()):
        print('Test passed.')
        sys.exit(0)
    print('Test failed.')
    sys.exit(1)
