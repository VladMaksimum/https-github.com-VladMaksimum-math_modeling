import matplotlib.pyplot as plt
import numpy as np

e=3
def log(b):
    f=np.arange(0,8*np.pi,0.01)
    r=e**(b*f)
    x=r*np.cos(f)
    y=r*np.sin(f)
    plt.plot(x,y)
    plt.savefig('pic_15.png')
log(20)

def arh(k):
    f=np.arange(0,8*np.pi,0.01)
    r=k*f
    x=r*np.cos(f)
    y=r*np.sin(f)
    plt.plot(x,y)
    plt.savefig('pic_16.png')
arh(20)

def zhez(k):
    f=np.arange(0.01,8*np.pi,0.01)
    r=k/(np.sqrt(f))
    x=r*np.cos(f)
    y=r*np.sin(f)
    plt.plot(x,y)
    plt.savefig('pic_17.png')
zhez(20)

def rosa(k):
    f=np.arange(0,8*np.pi,0.01)
    r=np.sin(k*f)
    x=r*np.cos(f)
    y=r*np.sin(f)
    plt.plot(x,y)
    plt.savefig('pic_18.png')
rosa(20)