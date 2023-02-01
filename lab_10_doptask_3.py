import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.arange(0,3,0.01)

def func(w,t):
    y,z = w
    dydt = z
    dzdt= (1-(z**2))**(1/2)
    return dydt, dzdt

y0 = 1
z0 = 0
w0 = y0, z0

risovalka=odeint(func, w0, t)

plt.plot(t, risovalka[:,0])
plt.plot(t, risovalka[:,1])
plt.savefig('pic8.png')