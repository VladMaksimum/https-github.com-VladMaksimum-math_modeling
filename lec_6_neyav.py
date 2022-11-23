import matplotlib.pyplot as plt
import numpy as np 

def circle(r=10):
    x = np.arange(-2*r, 2*r, 0.1)
    y = np.arange(-2*r, 2*r, 0.1)

    X, Y = np.meshgrid(x,y)

    fxy = X**2 + Y**2 - r**2

    plt.contour(X, Y, fxy, levels=[r**2])
    plt.axis('equal')
    plt.savefig('pic_4.png')
circle()
