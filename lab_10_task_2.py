import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.arange(-1,1,0.01)

def func(w,t):
    x, y=w
    dxdt= 3*x-2*y+((np.e**(3*t))/((np.e**t)+1))
    dydt= x - ((np.e**(3*t))/((np.e**t)+1))
    return dxdt, dydt

x0 = 5
y0 = -7
w0= x0, y0

risovalka=odeint(func, w0, t)

plt.plot(t,risovalka[:,0])
plt.plot(t,risovalka[:,1])
plt.savefig('pic3.png')