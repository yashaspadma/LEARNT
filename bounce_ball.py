import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 🎛️ Adjustable Parameters
gravity = -0.1     # Gravity force (negative for downward pull)
damping = 0.8      # Energy loss factor (1.0 = no loss, <1.0 = some loss)
ball_radius = 1     # Ball size
circle_radius = 10  # Boundary size
num_balls = 50    # Number of balls

# Randomly generate initial positions and velocities
np.random.seed(42)  # For consistent results
initial_positions = np.random.uniform(-circle_radius + ball_radius, 
                                      circle_radius - ball_radius, 
                                      (num_balls, 2))
initial_velocities = np.random.uniform(-3, 3, (num_balls, 2))

# Setup the figure and axes
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')  # Black background
ax.set_facecolor('black')
ax.set_xlim(-circle_radius, circle_radius)
ax.set_ylim(-circle_radius, circle_radius)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')

# Draw the circular boundary
circle = plt.Circle((0, 0), circle_radius, color='white', fill=False, linewidth=2)
ax.add_patch(circle)

# Create scatter plot for the balls
balls = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='green', s=200)

# Ball states
positions = np.array(initial_positions, dtype=float)
velocities = np.array(initial_velocities, dtype=float)

def update(frame):
    global positions, velocities

    for i in range(num_balls):  # Update each ball
        velocities[i][1] += gravity  # Apply gravity
        positions[i] += velocities[i]  # Update position

        # Check for collision with the circular boundary
        dist = np.linalg.norm(positions[i])  # Distance from center
        if dist + ball_radius >= circle_radius:
            normal = positions[i] / dist  # Compute normal at collision point
            velocities[i] -= 2 * np.dot(velocities[i], normal) * normal
            velocities[i] *= damping  # Apply damping
            positions[i] = normal * (circle_radius - ball_radius)  # Reposition inside boundary

    # Update scatter plot
    balls.set_offsets(positions)
    return balls,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=20, blit=True)

plt.show()
