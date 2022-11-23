import matplotlib.pyplot as plt
import numpy as np 

alpha = np.arange(-2*np.pi, 2*np.pi, 0.1)
r = 3

x = r*np.cos(alpha)
y = r*np.sin(alpha)
plt.xlim(-2*r, 2*r)
plt.ylim(-2*r, 2*r)

plt.savefig('pic_5.png')