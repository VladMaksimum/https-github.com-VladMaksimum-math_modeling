import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ball, = plt.plot([], [], "o")

def circle(r, vx0, vy0,time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange(0,2*np.pi,0.1)
    x= x0 + r*np.cos(alpha)
    y= y0 + r*np.sin(alpha)
    return x, y

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    ball.set_data(circle(r=2.5,vx0=0.01, vy0=0.01, time=i))
ani = FuncAnimation(fig,animate,frames=180,interval=30)
ani.save('lec_7_1.gif')