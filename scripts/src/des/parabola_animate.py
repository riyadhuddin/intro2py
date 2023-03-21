import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the dimensions of the area
length = 1000  # km
width = 500  # km

# Define the origin of the parabola
origin_x = length / 2  # km
origin_y = width / 2  # km

# Define the maximum height of the parabola
max_height = 15  # km
max_height_distance = width / 2  # km

# Define the parabolic equation
def parabola(x, t):
    a = max_height / max_height_distance**2
    return a * (x - origin_x)**2 + origin_y + t

# Generate x values for plotting
x = np.linspace(0, length, 1000)

# Define the animation function
def animate(t):
    # Generate y values for plotting at the given time
    y = parabola(x, t)

    # Clear the previous plot and plot the new curve
    plt.clf()
    plt.plot(x, y)

    # Set axis labels and title
    plt.xlabel('Distance (km)')
    plt.ylabel('Height (km)')
    plt.title('Parabolic Curve at Time t = {:.1f} km'.format(t))

# Create the animation object and display it
fig = plt.figure()
anim = FuncAnimation(fig, animate, frames=np.arange(0, 30, 0.1), interval=50)
plt.show()
