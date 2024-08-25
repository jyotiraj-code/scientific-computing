import random
import numpy as np

def estimate_pi(N):
    # Initialize the counter for points inside the unit quarter circle
    m = 0

    # Perform N random "shots"
    for _ in range(N):
        # Generate random x and y values between 0 and 1
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        # Check if the point (x, y) is inside the quarter circle
        if x**2 + y**2 <= 1:
            m += 1

    # Calculate the estimated value of pi
    pi_estimate = 4 * (m / N)
    return pi_estimate

# Number of random "shots" to perform
N = 1000000

# Estimate pi and print the result
pi_approximation = estimate_pi(N)
print(f"Approximated Pi: {pi_approximation} for N value of {N}")
print(f"The relative error percentage: {(pi_approximation - np.pi)*100 / np.pi}")

