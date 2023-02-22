import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

m=0.5
g=9.8
f=0.1
mu = 0.2
v=20

frames=200
t=np.linspace(0,100,frames)

def diff(w, t):
    x, vx, y, vy = w
    dxdt = vx
    dvxdt = 0
    dydt = vy
    dvydt = mu*m*vy - m*g
    return dxdt, dvxdt, dydt, dvydt

x0 = 0
v0x = v*np.cos(90)
y0 = 0
v0y = v*np.sin(90)
w0 = x0, v0x, y0, v0y

def move(i):
    risovalka = odeint(diff, w0, t)
    x = risovalka[i, 0]
    y = risovalka[i, 2]
    return x, y

fig, ax = plt.subplots()
ball, = plt.plot([], [])

def animate(i):
    ball.set_data(move(i))

ani = FuncAnimation(fig, animate, frames=frames, interval=30)

edge = 20
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.savefig('pic2.png')