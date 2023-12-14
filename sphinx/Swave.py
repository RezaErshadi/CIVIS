import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
grid_size = 100
shear_velocity = 1.0  # Shear wave velocity
frequency = 1.0  # Frequency of the source

# Function to initialize the shear wavefield
def initialize_shear_wavefield(grid_size):
    shear_wavefield = np.zeros((grid_size, grid_size))
    shear_wavefield[grid_size // 2, grid_size // 2] = 1.0  # Initial shear wave source
    return shear_wavefield

# Function to update the shear wavefield
def update_shear_wavefield(shear_wavefield, shear_velocity, dt):
    new_shear_wavefield = np.zeros_like(shear_wavefield)
    
    for i in range(1, shear_wavefield.shape[0] - 1):
        for j in range(1, shear_wavefield.shape[1] - 1):
            laplacian = (
                shear_wavefield[i + 1, j]
                + shear_wavefield[i - 1, j]
                + shear_wavefield[i, j + 1]
                + shear_wavefield[i, j - 1]
                - 4 * shear_wavefield[i, j]
            )
            new_shear_wavefield[i, j] = 2 * shear_wavefield[i, j] - new_shear_wavefield[i, j] + shear_velocity ** 2 * laplacian * dt ** 2

    return new_shear_wavefield

# Function to update the animation for shear waves
def update_shear_wave(frame):
    global shear_wavefield
    shear_wavefield = update_shear_wavefield(shear_wavefield, shear_velocity, dt)
    im.set_array(shear_wavefield)
    return im,

# Initialize the shear wavefield
shear_wavefield = initialize_shear_wavefield(grid_size)

# Set up the figure and axis
fig, ax = plt.subplots()
im = ax.imshow(shear_wavefield, cmap="viridis", animated=True)

# Set up animation parameters
dt = 0.01  # Time step
num_frames = 200

# Create the animation for shear waves
shear_animation = FuncAnimation(fig, update_shear_wave, frames=num_frames, interval=50, blit=True)

plt.show()
