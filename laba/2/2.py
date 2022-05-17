import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pylab
from textwrap import wrap

with open('vector_insert.txt','r') as v:
    v_ins = v.readlines()
    v_ins = list(map(int, v_ins))
with open('subvector_insert.txt','r') as sv:
    sv_ins = sv.readlines()
    sv_ins = list(map(int, sv_ins))
for i in range(len(v_ins)-1):
    if(np.abs(v_ins[i] - v_ins[i+1]) > 10):
        v_ins[i+1] = v_ins[i]
for i in range(len(sv_ins)-1):
    if(np.abs(sv_ins[i] - sv_ins[i+1]) > 10):
        sv_ins[i+1] = sv_ins[i]
fig, ax = pylab.subplots(figsize=(10, 10), dpi=75)
title = 'График зависимости insert t(n) для vector'
ax.set_title("\n".join(wrap(title, 100)), y=1)
plt.xlabel(r'n', fontsize=14)
plt.ylabel(r'mcsec', fontsize=14)
plt.plot(v_ins, color = 'red', label = 'vector')
ax.set_ylim(0,35)
ax.legend()
plt.savefig('t(n)v_ins.svg')
fig, ax = pylab.subplots(figsize=(10, 10), dpi=75)
title = 'График зависимости insert t(n) для subvector'
ax.set_title("\n".join(wrap(title, 100)), y=1)
plt.xlabel(r'n', fontsize=14)
plt.ylabel(r'mcsec', fontsize=14)
plt.plot(sv_ins, color = 'green', label = 'subvector')
ax.set_ylim(0,25)
ax.legend()
plt.savefig('t(n)sv_ins.svg')
plt.show()