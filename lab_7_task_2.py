import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
circle, = plt.plot([], [], "o")

def move(t,a):
    r=a*t
    alpha=np.arange(0,2*np.pi,0.1)
    alpha = np.arange(0,2*np.pi,0.1)
    x= r*np.cos(alpha)
    y= r*np.sin(alpha)
    return x,y

edge = 5
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    circle.set_data(move(t=i, a=0.01))
ani = FuncAnimation(fig,animate,frames=100,interval=15)
ani.save('lec_7_2.gif')