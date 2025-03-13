import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()
t = np.linspace(0, 3, 40) 
g = -9.81
v0 = 12
z = g * t**2 / 2 + v0 * t  

v02 = 5
z2 = g * t**2 / 2 + v02 * t  

line1, = ax.plot([], [], c="g", label=f'v0 = {v0} m/s')
line2, = ax.plot([], [], c="r", label=f'v0 = {v02} m/s')

ax.set(xlim=[0, 3], ylim=[0, 10], xlabel='Time [s]', ylabel='Z [m]')
ax.legend()

def update(frame):
    line1.set_data(t[:frame], z[:frame])
    line2.set_data(t[:frame], z2[:frame])
    return line1, line2

ani = animation.FuncAnimation(fig=fig, func=update, frames=len(t), interval=10)
plt.show()
