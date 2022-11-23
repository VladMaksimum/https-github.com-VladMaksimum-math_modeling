import matplotlib.pyplot as plt
import numpy as np

def parabola(a, b, c):
    x = np.arange(-8, 8, 0.1)
    y = a*x**2+b*x+c
    plt.plot(x,y)
    plt.axis('equal')
    plt.savefig('pic_7.png')
parabola(1,1,1)

def giperbola(a, b, c):
    for x in range(-8, 8, 1):
        y = (a/(x+b))+c
        d = x+b
        if d==0:
            continue
    plt.plot(x,y)
    plt.ylim(-8,8)
    plt.savefig('pic_8.png')
giperbola(1,1,1)