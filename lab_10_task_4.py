import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.arange(-5,5,0.01)

def func(w,t):
    y,z=w
    dydt = z
    dzdt = -4*z-5*y
    return dydt, dzdt

y0 = 4
z0 = -1
w0 = y0,z0

risovalka=odeint(func, w0, t)

plt.plot(t, risovalka[:,0])
plt.plot(t, risovalka[:,1])
plt.savefig('pic5.png')