import numpy as np
n = 5
m = 5
a = np.zeros((n, m))
for i in range(n):
  for j in range(m):
    b = np.sin(n * (i+1) + m * (j+1))
    if b < 0:
       a[i, j] = 0
    else:
      a[i, j] = b
print(a)