import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pylab
from textwrap import wrap

with open('vector_erase.txt','r') as v:
    v_era = v.readlines()
    v_era = list(map(int, v_era))
with open('subvector_erase.txt','r') as sv:
    sv_era = sv.readlines()
    sv_era = list(map(int, sv_era))
for i in range(len(v_era)-1):
    if(np.abs(v_era[i] - v_era[i+1]) > 10):
        v_era[i+1] = v_era[i]
for i in range(len(sv_era)-1):
    if(np.abs(sv_era[i] - sv_era[i+1]) > 10):
        sv_era[i+1] = sv_era[i]
'''fig, ax = pylab.subplots(figsize=(10, 10), dpi=75)
title = 'График зависимости erase t(n) для vector'
ax.set_title("\n".join(wrap(title, 100)), y=1)
plt.xlabel(r'n', fontsize=14)
plt.ylabel(r'mcsec', fontsize=14)
ax.set_ylim(0,80)
plt.plot(v_era, color = 'red', label = 'vector')
ax.legend()
plt.savefig('t(n)v_era.svg')'''

fig, ax = pylab.subplots(figsize=(10, 10), dpi=75)
title = 'График зависимости erase t(n) для subvector'
ax.set_title("\n".join(wrap(title, 100)), y=1)
plt.xlabel(r'n', fontsize=14)
plt.ylabel(r'mcsec', fontsize=14)
plt.plot(sv_era, color = 'green', label = 'subvector')
ax.set_ylim(0,85)
ax.legend()
plt.savefig('t(n)sv_era.svg')

plt.show()