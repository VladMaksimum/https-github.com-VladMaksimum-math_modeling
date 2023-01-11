import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
fractal, = plt.plot([], [], "o")

def move(n,x0,y0,c,d):
    if n=1:
        return 1
    
