import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x=np.arange(-5,5,0.1)

def func(w,x):
    y, z = w
    dydt = z
    dzdt = np.sin(x)+np.cos(x)
    return dydt, dzdt

y0 = 3
z0 = 0
w0 = y0, z0

risovalka=odeint(func, w0, x)

plt.plot(x, risovalka[:,0])
plt.plot(x, risovalka[:,1])
plt.savefig('pic4.png')