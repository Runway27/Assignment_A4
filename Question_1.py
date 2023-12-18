import numpy as np
import matplotlib.pyplot as plt

# Define the system matrix
A = np.array([[0.88, -0.2], [0.2, 0.88]])

# Define the initial state
x_0 = np.array([1.5,-1.5])  

# Initialize the state trajectory
x = np.zeros((50, 2)) #Initilizing a 2D array with 50 rows and 2 columns all filled with 0
x[0, :] = x_0 #This hold the colunm value of the above matrix. 

# Simulate the system
for t in range(49):
    x[t+1, :] = np.dot(A, x[t, :])

# Plot the state trajectory
plt.figure()
plt.plot(x[:, 0], label='x_1')
plt.plot(x[:, 1], label='x_2')
plt.xlabel('Time')
plt.ylabel('State')
plt.legend()
plt.show()

#Plot x1 vs x2
plt.figure()
plt.plot(x[:, 0], x[:, 1])
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()
