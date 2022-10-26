import lab_3_task_1 as t1
import numpy as np

h = 100
a = t1.pi/3
b = 30
d1 = t1.g * h *(np.tan(b))**2
d2 = 2 * (np.cos(a))**2
d3 = 1 - np.tan(b) * np.tan(a)
v = np.sqrt(d1/(d1*d1))
print(v)

t = 200
e = 300
d1 = 2/(np.sqrt(t1.pi))
d2 = t1.h/((t1.k*t)**(3/2))
d3 = t1.e**(-e/(t1.k*t))
d4 = e**(t/2)
n = d1 * d2 * d3 * d4
print(n)