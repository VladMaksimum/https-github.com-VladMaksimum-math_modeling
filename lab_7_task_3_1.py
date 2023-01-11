import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
heart, = plt.plot([], [], "o")
xdata, ydata = [], []

edge = 20
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def move(frame):
    xdata.append(16*np.sin(frame)**3)
    ydata.append(13*np.cos(frame)-5*np.cos(2*frame)-2*np.cos(3*frame)-np.cos(4*frame))
    heart.set_data(xdata, ydata)
    return heart,

ani = FuncAnimation(fig,move,frames=np.arange(0,2*np.pi,0.1),interval=10)
ani.save('lec_7_3_1.gif')