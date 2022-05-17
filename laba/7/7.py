import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pylab
from textwrap import wrap

with open('vector.txt','r') as v:
    vec = v.readlines()
    vec = list(map(int, vec))
for i in range(len(vec)-1):
    if(np.abs(vec[i] - vec[i+1]) > 20):
        vec[i+1] = vec[i]
with open('set.txt','r') as sett:
    Set = sett.readlines()
    Set = list(map(int, Set))
for i in range(len(Set)-1):
    if(np.abs(Set[i] - Set[i+1]) > 20):
        Set[i+1] = Set[i]
with open('map.txt','r') as mapp:
    Map = mapp.readlines()
    Map = list(map(int, Map))
for i in range(len(Map)-1):
    if(np.abs(Map[i] - Map[i+1]) > 20):
        Map[i+1] = Map[i]
with open('list.txt','r') as listt:
    listic = listt.readlines()
    listic = list(map(int, listic))
for i in range(len(listic)-1):
    if(np.abs(listic[i] - listic[i+1]) > 20):
        listic[i+1] = listic[i]
with open('forward_list.txt','r') as fl:
    forw_list = fl.readlines()
    forw_list = list(map(int, forw_list))
for i in range(len(forw_list)-1):
    if(np.abs(forw_list[i] - forw_list[i+1]) > 20):
        forw_list[i+1] = forw_list[i]
fig, ax = pylab.subplots(figsize=(10, 10), dpi=75)
title = 'График зависимости обхода t(n) для vector'
ax.set_title("\n".join(wrap(title, 100)), y=1)
plt.xlabel(r'n', fontsize=14)
plt.ylabel(r'mcsec', fontsize=14)
plt.plot(vec, color = 'red', label = 'vector')
ax.legend()
plt.savefig('t(n)v.svg')

'''fig, ax = pylab.subplots(figsize=(10, 10), dpi=75)
title = 'График зависимости обхода t(n) для set'
ax.set_title("\n".join(wrap(title, 100)), y=1)
plt.xlabel(r'n', fontsize=14)
plt.ylabel(r'mcsec', fontsize=14)
plt.plot(Set, color = 'blue', label = 'set')
ax.legend()
plt.savefig('t(n)s.svg')

fig, ax = pylab.subplots(figsize=(10, 10), dpi=75)
title = 'График зависимости обхода t(n) для map'
ax.set_title("\n".join(wrap(title, 100)), y=1)
plt.xlabel(r'n', fontsize=14)
plt.ylabel(r'mcsec', fontsize=14)
plt.plot(Map, color = 'green', label = 'map')
ax.legend()
plt.savefig('t(n)m.svg')

fig, ax = pylab.subplots(figsize=(10, 10), dpi=75)
title = 'График зависимости обхода t(n) для list'
ax.set_title("\n".join(wrap(title, 100)), y=1)
plt.xlabel(r'n', fontsize=14)
plt.ylabel(r'mcsec', fontsize=14)
plt.plot(listic, color = 'black', label = 'list')
ax.legend()
plt.savefig('t(n)l.svg')

fig, ax = pylab.subplots(figsize=(10, 10), dpi=75)
title = 'График зависимости обхода t(n) для forward_list'
ax.set_title("\n".join(wrap(title, 100)), y=1)
plt.xlabel(r'n', fontsize=14)
plt.ylabel(r'mcsec', fontsize=14)
plt.plot(forw_list, color = 'purple', label = 'forward_list')
ax.legend()
plt.savefig('t(n)f_l.svg')'''

plt.show()