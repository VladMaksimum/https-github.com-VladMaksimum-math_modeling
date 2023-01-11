import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
butterfly, = plt.plot([], [], "o")
xdata, ydata = [], []

edge = 5
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def move(frame):
    xdata.append(np.sin(frame)*(np.e**(np.cos(frame))-2*np.cos(4*frame)+(np.sin(frame/12))**5))
    ydata.append(np.cos(frame)*(np.e**(np.cos(frame))-2*np.cos(4*frame)+(np.sin(frame/12))**5))
    butterfly.set_data(xdata, ydata)
    return butterfly,

ani = FuncAnimation(fig,move,frames=np.arange(0,12*np.pi,0.09),interval=10)
ani.save('lec_7_3.gif')
