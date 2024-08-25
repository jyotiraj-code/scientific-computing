import random
import matplotlib.pyplot as plt

# Constants
N0 = 1000  # Initial number of parent nuclei
D0 = 0     # Initial number of daughter nuclei
p = 0.05   # Probability of decay (adjust as needed)
total_time = 100  # Total simulation time (adjust as needed)

# Lists to store data
time_points = []
n_values = []

# Initialize time
t = 0

# Main simulation loop
N = N0
D = D0
while N > 0 and t <= total_time:
    NU = N  # Number of undecayed nuclei at this time step
    for _ in range(NU):
        x = random.random()  # Generate a random number between 0 and 1
        if 0 < x <= p:
            N -= 1
            D += 1
    time_points.append(t)
    n_values.append(N)
    t += 1

# Plot the results
plt.plot(time_points, n_values, label='Number of Undecayed Nuclei')
plt.xlabel('Time')
plt.ylabel('Number of Undecayed Nuclei')
plt.title('Nuclear Decay Simulation')
plt.legend()
plt.grid(True)
plt.show()
