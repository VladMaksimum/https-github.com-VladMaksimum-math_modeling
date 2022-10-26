import lab_3_task_1 as t1
import numpy as np
x0 = int(input())
v0x = int(input())
y0 = int(input())
t = 0
x = x0 + v0x * t
y = y0 + v0x * t - ((t1.g * t**2)/2)
