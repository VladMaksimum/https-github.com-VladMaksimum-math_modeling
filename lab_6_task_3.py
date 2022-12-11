import matplotlib.pyplot as plt
import numpy as np

def elips(a,b):
    t = np.linspace(0, 2*np.pi, 100)
    plt.plot( a*np.cos(t) , b*np.sin(t) )
    plt.savefig('pic_14.png')
elips(8,8)