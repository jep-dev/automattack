#!/usr/bin/env python3

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

from util import *

def ltransform(f, x, *y):
    t = type(x)
    if(issubclass(t, list)):
        return [f(xi, *y) for xi in x]
    if(issubclass(t, tuple)):
        return (f(xi, *y) for xi in x)
    return None

def rtransform(f, x, y, *z):
    t = type(y)
    if(issubclass(t, list)):
        return [f(x, yi, *z) for yi in y]
    if(issubclass(t, tuple)):
        return (f(x, yi, *z) for yi in y)
    return None
