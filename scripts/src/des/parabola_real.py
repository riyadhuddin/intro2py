import pygame
import numpy as np

# define simulation parameters
time_step = 0.01
total_time = 10
n_steps = int(total_time / time_step)

# define physical constants
g = 9.81   # gravity constant
rho = 1000  # water density

# define environment
background_image = "img/bg.jpg"
screen_width = 800
screen_height = 600
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load(background_image).convert()

# define water droplet
diameter = 10  # diameter of water droplet in pixels
radius = diameter / 2
mass = (4 / 3) * np.pi * radius**3 * rho
initial_velocity = np.array([0, 0])  # initial velocity in pixels per second
position = np.array([100, 100], dtype=np.float64)  # initial position in pixels
acceleration = np.array([0, g]).reshape(2, 1)  # acceleration due to gravity

# define fluid dynamics
fluid_viscosity = 0.001
fluid_density = rho
fluid_drag = 6 * np.pi * fluid_viscosity * radius
fluid_lift = 0.5 * fluid_density * np.pi * radius**2

# create simulation loop
for i in range(n_steps):
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # update position and velocity of water droplet
    velocity = initial_velocity + acceleration * time_step
    position = position + velocity * time_step
    
    # update acceleration due to fluid dynamics
    velocity_norm = np.linalg.norm(velocity)
    drag_force = fluid_drag * velocity_norm * velocity / velocity_norm  # divide by velocity_norm to avoid broadcasting issues
    lift_force = fluid_lift * np.cross(np.array([0, 0, velocity_norm]), np.array([0, 0, 1]))[:2]  # slice to remove redundant dimension
    acceleration = np.array([0, g]).reshape(2, 1) - (drag_force + lift_force) / mass
    
    # check for collision with ground
    if (position[1] + radius >= screen_height).any():
        position[1] = screen_height - radius
        initial_velocity[1] *= -1
        
    # update screen
    screen.blit(background, (0, 0))
    # pygame.draw.circle(screen, (0, 0, 255), position.astype(int), radius)
    pygame.draw.circle(screen, (0, 0, 255), tuple(position.astype(int)), radius)
    pygame.display.update()
    pygame.time.delay(int(time_step * 1000))
