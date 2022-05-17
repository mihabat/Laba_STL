import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pylab
from textwrap import wrap

with open('cap.txt','r') as cap:
    capacity = cap.readlines()
    capacity = list(map(int, capacity))

with open('siz.txt','r') as siz:
    size = siz.readlines()
    size = list(map(int, size))

with open('subvector_cap.txt','r') as subcap:
    subcapacity = subcap.readlines()
    subcapacity = list(map(int, subcapacity))

with open('subvector_size.txt','r') as subsiz:
    subsize = subsiz.readlines()
    subsize = list(map(int, subsize))

fig, ax = pylab.subplots(figsize=(10, 10), dpi=75)
title = 'Графики зависимости size,capacity(n) для vector'
ax.set_title("\n".join(wrap(title, 100)), y=1)
plt.xlabel(r'n', fontsize=14)
plt.ylabel(r'размер', fontsize=14)
plt.plot(size, color = 'red', label = 'size')
plt.plot(capacity, color = 'blue', label = 'capacity')
ax.legend()
plt.savefig('cap,size(n).svg')

fig, ax = pylab.subplots(figsize=(10, 10), dpi=75)
title = 'Графики зависимости size,capacity(n) для subvector'
ax.set_title("\n".join(wrap(title, 100)), y=1)
plt.xlabel(r'n', fontsize=14)
plt.ylabel(r'размер', fontsize=14)
plt.plot(size, color = 'red', label = 'size')
plt.plot(capacity, color = 'green', label = 'capacity')
ax.legend()
plt.savefig('cap,size(n)sub.svg')
plt.show()


