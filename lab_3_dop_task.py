import numpy as np
str = 4
sto = 3
a  = np.zeros((str,sto))
c = np.zeros((str,sto))
b = np.ones((str,sto))
for i in range(str):
  for j in range(sto):
    if a[i,j]>b[i,j]:
      c[i,j] = a[i,j]
    else:
      c[i,j] = b[i,j]
print(c)