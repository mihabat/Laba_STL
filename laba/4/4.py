import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pylab
from textwrap import wrap

with open('vector_dostup.txt','r') as v:
    v_dos = v.readlines()
    v_dos = list(map(int, v_dos))
with open('subvector_dostup.txt','r') as sv:
    sv_dos = sv.readlines()
    sv_dos = list(map(int, sv_dos))
for i in range(len(v_dos)-1):
    if(np.abs(v_dos[i] - v_dos[i+1]) > 700):
        v_dos[i+1] = v_dos[i]
for i in range(len(sv_dos)-1):
    if(np.abs(sv_dos[i] - sv_dos[i+1]) > 700):
        sv_dos[i+1] = sv_dos[i]
'''fig, ax = pylab.subplots(figsize=(10, 10), dpi=75)
title = 'График зависимости доступа t(n) для vector'
ax.set_title("\n".join(wrap(title, 100)), y=1)
plt.xlabel(r'n', fontsize=14)
plt.ylabel(r'nanosec', fontsize=14)
plt.plot(v_dos, color = 'red', label = 'vector')
ax.set_ylim(0,1000)
ax.legend()
plt.savefig('t(n)v_dos.svg')'''

fig, ax = pylab.subplots(figsize=(10, 10), dpi=75)
title = 'График зависимости доступа t(n) для subvector'
ax.set_title("\n".join(wrap(title, 100)), y=1)
plt.xlabel(r'n', fontsize=14)
plt.ylabel(r'nanosec', fontsize=14)
plt.plot(sv_dos, color = 'green', label = 'subvector')
ax.legend()
plt.savefig('t(n)sv_dos.svg')

plt.show()