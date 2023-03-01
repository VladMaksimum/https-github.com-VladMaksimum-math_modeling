import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames=500
t=np.linspace(0, 5, frames)
k=125
m=0.5
g=9.8

def diff(w, t):
    y, vy = w 
    dydt = vy
    dvydt = (k/m)*y - g
    return dydt, dvydt

y0 = -0.08
vy0 = 0.5
w0 = y0, vy0

risovalka = odeint(diff, w0, t)

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o')

def animate(i):
    ball.set_data(0, risovalka[i, 0])

ani = FuncAnimation(fig, animate, frames=frames, interval=30)

edge = 100
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('lec_11_2.gif')