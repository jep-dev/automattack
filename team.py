#!/usr/bin/env python3

from util import *
from char import *
from time import sleep

__author__ = "John Petersen"
__version__ = "0.0.1"
__license__ = "GNU General Public License 3.0"

class Group(list):
    def transform(self, fn):
        return Group(fn(x) for x in self)
    def life(self):
        return Group(*[g for g in self if alive(g)])
    def death(self):
        return Group(*[g for g in self if not alive(g)])
    def __init__(self, *lst):
        super().__init__(l for l in lst)

class Teams:
    life = []
    death = []
    def __getitem__(self, k):
        return self.life[k]
    def __init__(self, *lst):
        life = [l for l in lst if dead(l)]
        death = [l for l in lst if not dead(l)]

#def fn_id(x, *args, **kwargs):
#    return x
#def fn_true(x, *args, **kwargs):
#    return True
#def fn_false(x, *args, **kwargs):
#    return False
#def fn_negation(f):
#    return lambda x, *args, **kwargs : not f(x)
#
#
#def transform(lst, fn = fn_id, pred = fn_true):
#    C = type(lst)
#    if(issubclass(C, dict)):
#        out = C()
#        for k,v in lst.items():
#            if(pred(v)):
#                out[k] = f(v)
#        return out
#    if(issubclass(C, (list, tuple))):
#        out = C()
#        for l in lst:
#            if(pred(l)):
#                out.append(l)
#        return out
#    return None


def chars(c):
    out = Group()
    t = type(c)
    if(issubclass(t, (list, tuple))):
        for ci in c:
            out.extend(chars(ci))
    elif(issubclass(t, dict)):
        for k,v in c.items():
            out.append(v)
    else:
        out.append(c)
    return out
