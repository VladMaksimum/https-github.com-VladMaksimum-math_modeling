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

a1 = np.zeros(n, m)
for i in range(n):
  for j in range(m):
    a1[i, j] = a[i, j]

a1[::,0], a1[::,1] = a[::,1], a[::,0]
print(a)
print(a1)