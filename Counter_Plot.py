import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate linearly spaced vectors
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# Create a meshgrid
X, Y = np.meshgrid(x, y)


# Define the function to plot
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))


# Compute Z values
Z = f(X, Y)

# Create a figure
fig = plt.figure(figsize=(8, 6))

# Add a 3D subplot
ax = fig.add_subplot(111, projection="3d")

# Plot a 3D contour
contour = ax.contour3D(X, Y, Z, 50, cmap="viridis")

# Add labels and a colorbar
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
fig.colorbar(contour, ax=ax, label="Z values")

# Show the plot
plt.show()
