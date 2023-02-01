import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.arange(-1,1,0.01)

def func(w,t):
    x,y,z=w
    dxdt = 3*x - y + z
    dydt = x+y+z
    dzdt = 4*x-y+4*z
    return dxdt, dydt, dzdt

x0=-71
y0 = 1
z0 = -3
w0 = x0, y0, z0

risovalka=odeint(func, w0, t)

plt.plot(t, risovalka[:,0])
plt.plot(t, risovalka[:,1])
plt.plot(t, risovalka[:,2])
plt.savefig('pic6.png')