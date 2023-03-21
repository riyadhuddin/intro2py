import numpy as np
import matplotlib.pyplot as plt

# Define the dimensions of the area
length = 1000  # km
width = 500  # km

# Define the origin of the parabola
origin_x = length / 2  # km
origin_y = width / 2  # km

# Define the maximum height of the parabola
max_height = 15  # km
max_height_distance = width / 2  # km

# Define the projectile's initial conditions
v0 = 1000  # m/s
theta = np.pi / 4  # radians
x0 = 0  # km
y0 = 0  # km

# Define constants
g = 9.81  # m/s^2
rho = 1.225  # kg/m^3 (air density at sea level)
Cd = 0.5  # drag coefficient
A = 0.01  # cross-sectional area of the projectile

# Define the parabolic equation
def parabola(x):
    a = max_height / max_height_distance**2
    return a * (x - origin_x)**2 + origin_y

# Define the function to calculate air resistance
def air_resistance(v, y):
    Fd = -0.5 * rho * v**2 * Cd * A
    return Fd

# Define the function to calculate the projectile's motion
def projectile_motion(t):
    # Convert time to seconds
    t = t * 60

    # Initialize variables
    x = x0
    y = y0
    vx = v0 * np.cos(theta)
    vy = v0 * np.sin(theta)
    ax = 0
    ay = -g
    dt = 0.01  # time step size
    total_time = 0

    # Simulate motion until the projectile hits the finish line
    while x < length:
        # Calculate air resistance
        v = np.sqrt(vx**2 + vy**2)
        Fd = air_resistance(v, y)
        ax = Fd / 100 / v0  # divided by 100 to convert kg to grams
        ay = -g + Fd / 100 / v0  # divided by 100 to convert kg to grams

        # Update velocity and position
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt

        # Update time
        total_time += dt

    # Return time taken to complete the course
    return total_time / 60  # convert back to minutes

# Generate x values for plotting
x = np.linspace(0, length, 1000)

# Generate y values for plotting
y = parabola(x)

# Plot the parabolic curve
plt.plot(x, y)

# Calculate the time taken for the projectile to complete the course
time_taken = projectile_motion(3)
print('Time taken:', time_taken, 'minutes')

# Set axis labels and title
plt.xlabel('Distance (km)')
plt.ylabel('Height (km)')
plt.title('Parabolic Curve with Projectile Motion')

# Display the plot
plt.show()
