import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
circle, = plt.plot([], [], "-")
e= 1.602176*10**(-19)

def move(t):
    t=np.arange(0,12*np.pi,0.1)
    x=np.sin(t)*(e**(np.cos(t)-2*np.cos(4*t)+(np.sin(t/12))**5))
    y=np.cos(t)*(e**(np.cos(t)-2*np.cos(4*t)+(np.sin(t/12))**5))
    return x,y

edge = 5
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    circle.set_data(move(t=i))
ani = FuncAnimation(fig,animate,frames=100,interval=15)
ani.save('lec_7_3.gif')
