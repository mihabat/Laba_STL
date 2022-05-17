import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pylab
from textwrap import wrap

with open('f_l_pop.txt','r') as f:
    f_pop = f.readlines()
    f_pop = list(map(int, f_pop))
with open('sfl_pop.txt','r') as sf:
    sf_pop = sf.readlines()
    sf_pop = list(map(int, sf_pop))
for i in range(len(f_pop)-1):
    if(np.abs(f_pop[i] - f_pop[i+1]) > 700):
        f_pop[i+1] = f_pop[i]
for i in range(len(sf_pop)-1):
    if(np.abs(sf_pop[i] - sf_pop[i+1]) > 700):
        sf_pop[i+1] = sf_pop[i]
fig, ax = pylab.subplots(figsize=(10, 10), dpi=75)
title = 'График зависимости pop_front t(n) для forward_list'
ax.set_title("\n".join(wrap(title, 100)), y=1)
plt.xlabel(r'n', fontsize=14)
plt.ylabel(r'nanosec', fontsize=14)
plt.plot(f_pop, color = 'red', label = 'forward_list')
ax.legend()
plt.savefig('t(n)f_pop.svg')

fig, ax = pylab.subplots(figsize=(10, 10), dpi=75)
title = 'График зависимости pop_front t(n) для subforward_list'
ax.set_title("\n".join(wrap(title, 100)), y=1)
plt.xlabel(r'n', fontsize=14)
plt.ylabel(r'nanosec', fontsize=14)
plt.plot(sf_pop, color = 'green', label = 'subforward_list')
ax.legend()
plt.savefig('t(n)sf_pop.svg')

plt.show()