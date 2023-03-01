import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

k1 = 3
k2 = 5
A=100

t=np.arange(0,5,0.1)

def diff(w,t):
    X, Y = w
    dxdt = k1*(A-X-Y)
    dydt = k2*(A-X-Y)
    return dxdt, dydt

X0=0
Y0=0
w0= X0, Y0

risovalka = odeint(diff, w0, t)

plt.plot(t, risovalka[:,0])
plt.plot(t, risovalka[:,1])
plt.savefig('pic1.png')