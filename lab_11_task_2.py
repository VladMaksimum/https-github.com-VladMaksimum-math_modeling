import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

A=8000
k1 = 5
k2 =10

frames = 200
t=np.linspace(0,5,frames)

def diff(w,t):
    x, y = w
    dxdt 