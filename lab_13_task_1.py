import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 365
seconds_in_year = 365 * 24 * 60 * 60
seconds_in_day = 24 * 60 * 60
years = 0.5
t = np.linspace(0, years*seconds_in_year, frames)

ae = 149 * 10**9
M =  1.98847 * 10**30 
ma = 1.06 * M
mb = 0.96 * M
mc = 0.67 * M
G = 6.67 * 10 **(-11)

def move(w, t):
    (xa, v_xa, ya, v_ya,
    xb, v_xb, yb, v_yb,
    xc, v_xc, yc, v_yc) = w

    dxdta = v_xa
    dv_xdta = (
      	    - G * mb * (xa - xb) 
               / ((xa - xb)**2 + (ya - yb)**2)**1.5
            - G * mc * (xa - xc) 
               / ((xa - xc)**2 + (ya - yc)**2)**1.5
             )
    dydta = v_ya
    dv_ydta = (
      	    - G * mb * (ya - yb) 
               / ((xa - xb)**2 + (ya - yb)**2)**1.5
            - G * mb * (ya - yc) 
               / ((xa - xc)**2 + (ya - yc)**2)**1.5
            )
    
    dxdtb = v_xb
    dv_xdtb = (
      	    - G * ma * (xb - xa) 
               / ((xb - xa)**2 + (yb - ya)**2)**1.5
            - G * mc * (xb - xc) 
               / ((xb - xc)**2 + (yb - yc)**2)**1.5
            )

    dydtb = v_yb
    dv_ydtb = (
      	    - G * ma * (yb - ya) 
               / ((xb - xa)**2 + (yb - ya)**2)**1.5
            - G * mb * (yb - yc) 
               / ((xb - xc)**2 + (yb - yc)**2)**1.5
    	      )
    
    dxdtc = v_xc
    dv_xdtc = (
      	    - G * ma * (xc - xa) 
               / ((xc - xa)**2 + (yc - ya)**2)**1.5
            - G * mb * (xc - xb) 
               / ((xc - xb)**2 + (yc - yb)**2)**1.5
             )
    dydtc = v_yc
    dv_ydtc = (
      	    - G * ma * (yc - ya) 
               / ((xc - xa)**2 + (yc - ya)**2)**1.5
            - G * mb * (yc - yb) 
               / ((xc - xb)**2 + (yc - yb)**2)**1.5
            )
    return (dxdta, dv_xdta, dydta, dv_ydta,
    dxdtb, dv_xdtb, dydtb, dv_ydtb,
    dxdtc, dv_xdtc, dydtc, dv_ydtc,  )

xa0 = 0
v_xa0 = 8638
ya0 = 0
v_ya0 = 0

xb0 = 12.3 * ae
v_xb0 = 0
yb0 = 0
v_yb0 = 6000

xc0 = (12.3 + 0.67) * ae
v_xc0 = 0
yc0 = 0
v_yc0 = 4000

w0 = (xa0, v_xa0, ya0, v_ya0,
xb0, v_xb0, yb0, v_yb0,
xc0, v_xc0, yc0, v_yc0)

sol = odeint(move, w0, t)

def a(i):
    

fig, ax = plt.subplots()

a_move, = plt.plot([], [], 'o', color='y')
b_move, = plt.plot([], [], 'o', color='b')
c_move, = plt.plot([], [], 'o', color='r')

def animate(i):
    a_move.set_data(a(i))
    b_move.set_data(b(i))
    c_move.set_data(c(i))


ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)
 
plt.axis('equal')
edge = 2 * xc0
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
ani.save('lab_13_task_1.gif')
