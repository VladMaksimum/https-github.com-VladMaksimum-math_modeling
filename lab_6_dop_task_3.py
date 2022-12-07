import numpy as np
import matplotlib.pyplot as plt
def kusok(x,a,b):
    y=np.zeros(len(x))
    for i in range(len(x)):
        if x[i]<a:
            y[i]= a**2
        elif x[i]>=a and x[i]<=b:
            y[i]= x[i]**2
        else:
            y[i]= b**2
        return y

a=-5
b=8
x=np.linspace(-10,10,100)
y=kusok(x,a,b)
plt.plot(x,y)
plt.savefig('pic_10.png')