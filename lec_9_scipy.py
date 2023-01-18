import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt 

t= np.arange(0,10**6,100)

def radio(m,t):
    dmdt= -k * m
    return dmdt

m_0= 10
k = 1.61 * 10**(-6)

m_t  = odeint(radio, m_0, t)

plt.plot(t,m_t[:,0])
plt.savefig('pic1.png')