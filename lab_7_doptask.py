import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
star, = plt.plot([], [], "o")

def move(T):
    t=np.arange(0,4*np.pi,0.1)
    x=12*np.cos(t)+8*np.cos(1.5*t)
    y=12*np.sin(t)-8*np.sin(1.5*t)

    X=x*np.cos(T)-y*np.sin(T)
    Y=y*np.cos(T)+x*np.sin(T)
 
edge = 25
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    star.set_data(move(T=i))
ani = FuncAnimation(fig,animate,frames=np.arange(0,4*np.pi,0.1),interval=10)
ani.save('lec_7_dop.gif')