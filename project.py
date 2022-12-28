import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
def planet_track(r=1):
    x = np.arange(-2*r, 2*r, 0.1)
    y = np.arange(-2*r, 2*r, 0.1)

    X, Y = np.meshgrid(x,y)

    fxy = X**2 + Y**2 - r**2

    plt.contour(X, Y, fxy, levels=[r**2])
    plt.axis('equal')
    plt.savefig('pic.png')
planet_track()

def sun(r=0.25):
    x = np.arange(-2*r, 2*r, 0.1)
    y = np.arange(-2*r, 2*r, 0.1)

    X, Y = np.meshgrid(x,y)

    fxy = X**2 + Y**2 -r**2

    plt.contour(X, Y, fxy, levels=[r**2])
    plt.axis('equal')
    plt.savefig('pic.png')
sun()

def earth(r=0.25):
    x = np.arange(-2*r, 2*r, 0.1)
    y = np.arange(-2*r, 2*r, 0.1)

    X, Y = np.meshgrid(x,y)

    fxy = X**2 + Y**2 - r**2

    plt.contour(X, Y+1.5, fxy, levels=[r**2])
    plt.axis('equal')
    plt.savefig('pic.png')
earth()

def earth_track(r=2):
    x = np.arange(-2*r, 2*r, 0.1)
    y = np.arange(-2*r, 2*r, 0.1)

    X, Y = np.meshgrid(x,y)

    fxy = X**2 + Y**2 - r**2

    plt.contour(X, Y, fxy, levels=[r**2])
    plt.axis('equal')
    plt.savefig('pic.png')
earth_track()

def racket_track(r=1.5):
    x = np.arange(-2*r, 2*r, 0.1)
    y = np.arange(-2*r, 2*r, 0.1)

    X, Y = np.meshgrid(x,y)

    fxy = X**2 + Y**2 - r**2

    plt.contour(X, Y-0.7, fxy, levels=[r**2])
    plt.axis('equal')
    plt.savefig('pic.png')
racket_track()

planet,=plt.plot([], [] ,'o')
def move_planet(r, angle_vel, time):
    alpha = angle_vel * (np.pi/180) * time + 3
    x=r*np.cos(alpha)
    y=r*np.sin(alpha)
    return x, y

edge = 5
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    planet.set_data(move_planet(r=2.83,angle_vel=1, time=i))
ani = FuncAnimation(fig,animate,frames=90,interval=15)
ani.save('project.gif')

racket,=plt.plot([], [] ,'o')
def move_racket(r, angle_vel, time):
    alpha = angle_vel * (np.pi/180) * time + 1.5
    x=r*np.cos(alpha)
    y=r*np.sin(alpha)-0.7
    return x, y

edge = 5
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    racket.set_data(move_racket(r=2.1,angle_vel=1.9, time=i))
ani = FuncAnimation(fig,animate,frames=90,interval=15)
ani.save('project.gif')