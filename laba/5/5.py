import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pylab
from textwrap import wrap

with open('f_l_push.txt','r') as f:
    f_push = f.readlines()
    f_push = list(map(int, f_push))
with open('sfl_push.txt','r') as sf:
    sf_push = sf.readlines()
    sf_push = list(map(int, sf_push))
for i in range(len(f_push)-1):
    if(np.abs(f_push[i] - f_push[i+1]) > 700):
        f_push[i+1] = f_push[i]
for i in range(len(sf_push)-1):
    if(np.abs(sf_push[i] - sf_push[i+1]) > 700):
        sf_push[i+1] = sf_push[i]
fig, ax = pylab.subplots(figsize=(10, 10), dpi=75)
title = 'График зависимости push_front t(n) для forward_list'
ax.set_title("\n".join(wrap(title, 100)), y=1)
plt.xlabel(r'n', fontsize=14)
plt.ylabel(r'nanosec', fontsize=14)
plt.plot(f_push, color = 'red', label = 'forward_list')
ax.legend()
plt.savefig('t(n)f_push.svg')

fig, ax = pylab.subplots(figsize=(10, 10), dpi=75)
title = 'График зависимости push_front t(n) для subforward_list'
ax.set_title("\n".join(wrap(title, 100)), y=1)
plt.xlabel(r'n', fontsize=14)
plt.ylabel(r'nanosec', fontsize=14)
plt.plot(sf_push, color = 'green', label = 'subforward_list')
ax.legend()
plt.savefig('t(n)sf_push.svg')

plt.show()