import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x=np.arange(0,5,0.1)

def func(w,x):
    y,z = w
    dydx = z
    dzdx = (z**2-((3*y**2)/x**(1/2)))/y
    return dydx, dzdx

y0 = 0
z0 = 1
w0 = y0, z0

risovalka=odeint(func, w0, x)

plt.plot(x, risovalka[:,0])
plt.plot(x, risovalka[:,1])
plt.savefig('pic7.png')