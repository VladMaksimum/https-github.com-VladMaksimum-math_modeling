import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.animation import FuncAnimation

t= np.arange(1,10,0.1)
r=5
x=r*(t-(np.sin(t)**2))
y=r*(1-(np.cos(t)**2))

x1=r*(np.sin(t)**3)
y1=r*(np.cos(t)**3)

plt.plot(x1,y1)
plt.savefig('pic_12.png')
