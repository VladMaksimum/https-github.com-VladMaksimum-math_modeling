import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

m=0.5
g=9.8
f=0.1
mu = 0.2

frames=200
t=np.linspace(0,5,frames)

def diff(w, t):
    y, vy = w
    dydt = vy
    dvydt = -mu*m*vy - g
    return dydt, dvydt

y0 = 0
v0y = 20
w0 = y0, v0y

def move(i):
    risovalka = odeint(diff, w0, t)
    x = 0
    y = risovalka[i, 0]
    return  x, y

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o')

def animate(i):
    ball.set_data(move(i))

ani = FuncAnimation(fig, animate, frames=frames, interval=30)

edge = 20
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('lec_11_1.gif')