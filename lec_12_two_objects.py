import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
frames = 365
seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, years*seconds_in_year, frames)

def move_func(s, t):
    (x1, v_x1, y1, v_y1,
    x2, v_x2, y2, v_y2) = s
    
    dx1dt = v_x1
    dv_x1dt = - G * m * x1 / (x1**2 + y1**2)**1.5
    dy1dt = v_y1
    dv_y1dt = - G * m * y1 / (x1**2 + y1**2)**1.5
    dx2dt = v_x2
    dv_x2dt = - G * m * x2 / (x2**2 + y2**2)**1.5
    dy2dt = v_y2
    dv_y2dt = - G * m * y2 / (x2**2 + y2**2)**1.5
    
    return (dx1dt, dv_x1dt, dy1dt, dv_y1dt,
    dx2dt, dv_x2dt, dy2dt, dv_y2dt)

G = 6.67 * 10**(-11)
m = 1.98 * 10**(30)

x10 = 149 * 10**9
v_x10 = 0
y10 = 0
v_y10 = 30000

x20 = 0
v_x20 = -48000
y20 = 58 * 10**9
v_y20 = 0

s0 = (x10, v_x10, y10, v_y10,
x20, v_x20, y20, v_y20)

sol = odeint(move_func, s0, t)

def earth(i):
    x1= sol[i, 0]
    y1= sol[i, 2]
    return x1, y1

def mercure(i):
    x2= sol[i, 4]
    y2= sol[i, 6]
    return x2, y2

fig, ax = plt.subplots()

plt.plot([0], [0], 'o', color='y', ms=20)
earth_move, = plt.plot([], [], 'o', color='g')
mercure_move, = plt.plot([], [], 'o', color='b')

def animate(i):
    earth_move.set_data(earth(i))
    mercure_move.set_data(mercure(i))

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

plt.axis('equal')
edge = 2*x10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('earth_mercure.gif')