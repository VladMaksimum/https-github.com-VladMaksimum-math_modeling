import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt 

t = np.arange(0,10,0.001)

def bact(n,t):
    dndt = k * n
    return dndt

n_0 = 1
k = 2
n_t = odeint(bact, n_0, t)

plt.plot(t, n_t[:,0])
plt.savefig('pic2.png')