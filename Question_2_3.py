import matplotlib.pyplot as plt
from scipy.linalg import solve_discrete_lyapunov 
import numpy as np
#Input the matrix
a = np.array([[0.8, 0.6], [-0.7, 0.3]])
q = np.eye(2)
#Solve for A^TPA-P=-I
p = solve_discrete_lyapunov(a.T, q)
print(p)
###############################################################################
#Plotting of the ellipsoidal set
energy=np.dot(a.T, p, a)
# Generate theta values
theta = np.linspace(0, 2*np.pi, 100)
#theta generates 100 equally spaced values between 0 to 2pi
# Generate the points on the surface of the unit sphere
x = np.cos(theta)
y = np.sin(theta)
points = np.vstack((x, y))

# Transform energy to get points on the ellipsoid
ellipsoid_points = np.dot(energy, points)

# Plot the ellipsoid
plt.figure()
plt.plot(ellipsoid_points[0, :], ellipsoid_points[1, :])
plt.title('Ellipsoidal Invariant Set')
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()