import numpy as np
t = np.arange(1, 5, 1)
def sred_arifm():
  x = sum(t)/len(t)
  return x
print(sred_arifm())