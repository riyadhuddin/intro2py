import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1000)
ax.set_ylim(0, 500)

# Set up the water drop
water_size = 10  # Diameter of the water drop
water_velocity = 50  # Velocity of the water drop
water_mass = 100  # Mass of the water drop
water_density = 1000  # Density of water
water_volume = water_mass / water_density  # Volume of the water drop
water_area = np.pi * (water_size / 2) ** 2  # Surface area of the water drop

# Set up the ground surface
ground_height = 0
ground_length = 1000
ground_width = 500

# Set up the simulation parameters
time_step = 0.1  # Time step for simulation
time = 0  # Initial time
total_time = 10  # Total time for simulation

# Create the water drop
water_x = np.random.uniform(0, ground_length)  # Random x-coordinate for water drop
water_y = ground_height  # Initial y-coordinate for water drop
water_vy = water_velocity  # Initial velocity for water drop in y-direction
water_ax = 0  # Initial acceleration for water drop in x-direction
water_ay = -9.8  # Initial acceleration for water drop in y-direction

# Create the scatter plot for the water drop
water_scatter = ax.scatter(water_x, water_y, s=water_size, alpha=0.5)

# Create the ground surface
ground = plt.Rectangle((0, 0), ground_length, ground_width, facecolor='green', alpha=0.5)
ax.add_patch(ground)

# Define the update function for the animation
def update(frame):
    global water_x, water_y, water_vy, water_ax, water_ay, time
    time += time_step

    # Update the position and velocity of the water drop
    water_x += water_velocity * time_step
    water_y += water_vy * time_step
    water_vx = water_ax * time_step
    water_vy += water_ay * time_step

    # Check if the water drop hits the ground
    if water_y < ground_height + water_size / 2:
        water_vy = -water_vy * 0.5

    # Update the scatter plot for the water drop
    water_scatter.set_offsets([water_x, water_y])

    # Return the scatter plot
    return water_scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, total_time, time_step), interval=10)

# Show the animation
plt.show()
