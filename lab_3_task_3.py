import lab_3_task_1 as t1
import numpy as np
x0 = int(input())
y0 = int(input())
v0x = int(input())
t = np.arange(0, 5, 1)
x = x0 + v0x * t
y = y0 + v0x * t - ((t1.g * t**2) / 2)
coords = np.zeros((6, 3))
for i in range(0, 6, 1):
  coords[i, 0] = t[i]
  coords[i, 1] = x[i]
  coords[i, 2] = y[i]
print(coords)