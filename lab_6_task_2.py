import matplotlib.pyplot as plt
import numpy as np

def parabola(a,b,c):
    x = np.arange(-8, 8, 0.1)
    y = a*x**2+b*x+c
    plt.plot(x,y)
    plt.axis('equal')
    plt.savefig('pic_7.png')
parabola(1,1,1)

def giperbola(a):
    x1= np.arange(-8,-0.01,0.01)
    x2= np.arange(0.01,8,0.01)
    y1=1/x1
    y2=1/x2
    plt.plot(x1,y1)
    plt.plot(x2,y2)
    plt.ylim(-8,8)
    plt.savefig('pic_8.png')
giperbola(1)