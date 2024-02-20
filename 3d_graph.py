import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import solidmechanics as sima

# Placeholder for generating combinations and corresponding dt values

# Iterating through each combination of parameters
dt_list = sima.get_result(sima.theta, sima.h_2, sima.e, sima.l)                 


# Convert lists to numpy arrays for consistent data handling
theta_array = sima.theta
h2_array = sima.h_2
e_array = sima.e
dt_array = dt_list
l_array = np.array(sima.l)


# Normalize l values to use as size for the scatter plot points
sizes = (l_array - min(l_array)) / (max(l_array) - min(l_array)) * 100  # Adjust the scaling factor as necessary

# Create the 3D scatter plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(theta_array, h2_array, dt_array, c=e_array, cmap='viridis', s=sizes)

# Labeling the axes
ax.set_xlabel('Launch Angle (theta)')
ax.set_ylabel('Initial Height (h2)')
ax.set_zlabel('Distance Traveled (dt)')

# Add a color bar to indicate the scale of the coefficient of restitution 'e'
color_bar = fig.colorbar(scatter, ax=ax)
color_bar.set_label('Coefficient of Restitution (e)')

plt.show()
