import numpy as np
t = np.zeros((5, 2))
x = np.arange(1, 6)
def cvadratnaya(t):
  for i in range(5):
    y = x[i]**2
    t[i, 0] = y
    t[i, 1] = x[i]
  return t
print(cvadratnaya(t))