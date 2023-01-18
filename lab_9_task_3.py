import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.arange(0, 50, 0.1)

def sopr(v,t):
    dvdt = -(m*g - v*y)/m
    return dvdt

y=5
m=60
g=10
v0=100
v_t=odeint(sopr, v0, t)

plt.plot(t, v_t[:,0])
plt.savefig('pic4.png')