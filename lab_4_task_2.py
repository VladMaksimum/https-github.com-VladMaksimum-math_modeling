import numpy as np
t = np.arange(1, 5)

def peremnozh(t):
  a1 = 1
  for i in t:
    a1 = a1 * i
  return a1
print(peremnozh(t))