import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
frames = 365
seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, years*seconds_in_year, frames)

G = 6.67 * 10**(-11)
m = 1.98 * 10**(30)

def move_func(s, t):
    (xe, v_xe, ye, v_ye,
    xme, v_xme, yme, v_yme, 
    xma, v_xma, yma, v_yma,
    xv, v_xv, yv, v_yv,
    xf, v_xf, yf, v_yf) = s
    
    dxedt = v_xe
    dv_xedt = - G * m * xe / (xe**2 + ye**2)**1.5
    dyedt = v_ye
    dv_yedt = - G * m * ye / (xe**2 + ye**2)**1.5
    dxmedt = v_xme
    dv_xmedt = - G * m * xme / (xme**2 + yme**2)**1.5
    dymedt = v_yme
    dv_ymedt = - G * m * yme / (xme**2 + yme**2)**1.5
    dxmadt = v_xma
    dv_xmadt = - G * m * xma / (xma**2 + yma**2)**1.5
    dymadt = v_yma
    dv_ymadt = - G * m * yma / (xma**2 + yma**2)**1.5
    dxvdt = v_xv
    dv_xvdt = - G * m * xv / (xv**2 + yv**2)**1.5
    dyvdt = v_yv
    dv_yvdt = - G * m * yv / (xv**2 + yv**2)**1.5
    dxfdt = v_xf
    dv_xfdt = - G * m * xf / (xf**2 + yf**2)**1.5
    dyfdt = v_yf
    dv_yfdt = - G * m * yf / (xf**2 + yf**2)**1.5
    
    return (dxedt, dv_xedt, dyedt, dv_yedt,
    dxmedt, dv_xmedt, dymedt, dv_ymedt,
    dxmadt, dv_xmadt, dymadt, dv_ymadt,
    dxvdt, dv_xvdt, dyvdt, dv_yvdt,
    dxfdt, dv_xfdt, dyfdt, dv_yfdt)

xe0 = 149 * 10**9
v_xe0 = 0
ye0 = 0
v_ye0 = 30000

xme0 = 0
v_xme0 = -48000
yme0 = 58 * 10**9
v_yme0 = 0

xma0 = 0
v_xma0 = 24000
yma0 = 228 * 10**9
v_yma0 = 0

xv0 = 108 * 10**9
v_xv0 = 0
yv0 = 0
v_yv0 = 35000

xf0 = 190 * 10**12
v_xf0 = 0
yf0 = 0
v_yf0 = 20122

s0 = (xe0, v_xe0, ye0, v_ye0,
xme0, v_xme0, yme0, v_yme0,
xma0, v_xma0, yma0, v_yma0,
xv0, v_xv0, yv0, v_yv0,
xf0, v_xf0, yf0, v_yf0)

sol = odeint(move_func, s0, t)

def earth(i):
    x= sol[i, 0]
    y= sol[i, 2]
    return x, y

def mercure(i):
    x= sol[i, 4]
    y= sol[i, 6]
    return x, y

def mars(i):
    x= sol[i, 8]
    y= sol[i, 10]
    return x,y

def venera(i):
    x= sol[i, 12]
    y= sol[i, 14]
    return x, y

def faeton(i):
    x= sol[i, 16]
    y= sol[i, 18]
    return x, y

fig, ax = plt.subplots()

plt.plot([0], [0], 'o', color='y', ms=20)
earth_move, = plt.plot([], [], 'o', color='g')
mercure_move, = plt.plot([], [], 'o', color='b')
mars_move, = plt.plot([], [], 'o', color='r')
venera_move, = plt.plot([], [], 'o', color='m')
faeton_move, = plt.plot([], [], 'o', color='c')

def animate(i):
    earth_move.set_data(earth(i))
    mercure_move.set_data(mercure(i))
    mars_move.set_data(mars(i))
    venera_move.set_data(venera(i))
    faeton_move.set_data(faeton(i))

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

plt.axis('equal')
edge = 2*250*10**9
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('eartn_planets.gif')