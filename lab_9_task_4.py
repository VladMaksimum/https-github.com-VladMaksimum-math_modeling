import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t= np.arange(0,10, 0.01)

def zacon(f,t):
    dvdt = (b-k*t)/m
    return dvdt

b= 10
k= 5
v0 = 8

v_t=odeint(zacon, v0, t)

plt.plot(t, f_t[:,0])
plt.savefig('pic5.png')