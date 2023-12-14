import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from obspy.core import Trace, Stream, UTCDateTime

# Define the seismic wave velocity profile
depth = np.linspace(0, 100, 100)  # Depth in kilometers
velocity = 6.5  # P-wave velocity in kilometers per second
time = depth / velocity  # Travel time calculation

# Create the animation
fig, ax = plt.subplots()
line, = ax.plot(depth, time)

def animate(i):
    line.set_ydata(time + i)  # Simulate wave propagation
    return line,

ani = animation.FuncAnimation(fig, animate, frames=20, interval=100, blit=True)
plt.xlabel('Depth (km)')
plt.ylabel('Travel Time (s)')
plt.show()