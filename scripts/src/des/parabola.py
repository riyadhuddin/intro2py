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

# Define the parabolic equation
def parabola(x):
    a = max_height / max_height_distance**2
    return a * (x - origin_x)**2 + origin_y

# Generate x values for plotting
x = np.linspace(0, length, 1000)

# Generate y values for plotting
y = parabola(x)

# Plot the parabola
plt.plot(x, y)

# Set axis labels and title
plt.xlabel('Distance (km)')
plt.ylabel('Height (km)')
plt.title('Parabolic Curve')

# Display the plot
plt.show()
