import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt 

t=np.arange(0,4,0.001)

def proizvod(invest, t):
    dsdt = -k * invest * t
    return dsdt

invest_0 = 1000
k= 0.08
invest_t=odeint(proizvod, invest_0, t)

plt.plot(t, invest_t[:,0])
plt.savefig('pic3.png')