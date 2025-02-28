import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# 🎛️ Adjustable Parameters
gravity = np.array([0, 0, -0.02])  # Gravity force (affects Z-axis)
damping = 0.9      # Energy loss factor (1.0 = no loss, <1.0 = damping)
sphere_radius = 10  # Radius of the spherical boundary
ball_radius = 1     # Ball size

# Initial position and velocity
np.random.seed(42)
position = np.random.uniform(-sphere_radius / 2, sphere_radius / 2, 3)
velocity = np.random.uniform(-2, 2, 3)

# Setup the figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', facecolor='black')
ax.set_xlim([-sphere_radius, sphere_radius])
ax.set_ylim([-sphere_radius, sphere_radius])
ax.set_zlim([-sphere_radius, sphere_radius])
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_box_aspect([1, 1, 1])  # Equal aspect ratio

# Draw the spherical boundary
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
sphere_x = sphere_radius * np.cos(u) * np.sin(v)
sphere_y = sphere_radius * np.sin(u) * np.sin(v)
sphere_z = sphere_radius * np.cos(v)
ax.plot_wireframe(sphere_x, sphere_y, sphere_z, color="white", alpha=0.3)

# Create the ball
ball, = ax.plot([], [], [], 'go', markersize=10)

def update(frame):
    global position, velocity

    # Apply gravity
    velocity += gravity
    position += velocity

    # Check for collision with the sphere boundary
    dist = np.linalg.norm(position)
    if dist + ball_radius >= sphere_radius:
        normal = position / dist  # Normal vector at collision point
        velocity -= 2 * np.dot(velocity, normal) * normal  # Reflect velocity
        velocity *= damping  # Apply damping
        position = normal * (sphere_radius - ball_radius)  # Keep inside boundary

    # Update ball position (✅ Fixed)
    ball.set_data([position[0]], [position[1]])
    ball.set_3d_properties([position[2]])
    return ball,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=500, interval=20, blit=True)

plt.show()
