import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x= np.arange(-5,5,0.1)

def func(w,x):
    y, z=w
    dydx= y**2*z
    dzdx= (z/x)- (y*z**2)
    return dydx, dzdx

y0=1
z0=-3
w0=y0, z0

risovalka=odeint(func, w0, x)

plt.plot(x, risovalka[:,0])
plt.plot(x, risovalka[:,1])
plt.savefig('pic2.png')