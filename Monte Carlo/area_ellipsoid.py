#Importing the dependencies

import random
import numpy as np

def estimate_ellipsoid_volume(M, N, a, b, c):
    #Initializing the values of the sum and sum of squares
    SUM = 0
    SUM2 = 0

    # Perform M measurements
    for _ in range(M):
        # Initialize the counter for points inside the ellipsoid
        count = 0

        # Perform N random "shots"
        for _ in range(N):
            # Generate three random numbers between 0 and 1
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            z = random.uniform(0, 1)

            # Check if the point (x, y, z) is inside the ellipsoid
            if (x**2 / a**2) + (y**2 / b**2) + (z**2 / c**2) <= 1:
                count += 1

        # Calculate the volume for this measurement
        dv = 1 / N
        volume = (8 * a * b * c * count) / (N * dv)

        # Increment the sum and sum of squares
        SUM += volume
        SUM2 += volume**2

    # Calculate the average volume
    average_volume = SUM / M

    # Calculate the standard deviation
    std_deviation = np.sqrt((SUM2 / M) - (average_volume**2))

    return average_volume, std_deviation

# Input parameters
M = 25          # Number of measurements
N = 1000        # Number of random points per measurement
a = 2.0         # Semi-major axis length
b = 1.5         # Semi-intermediate axis length
c = 1.0         # Semi-minor axis length

# Estimate the ellipsoid volume and standard deviation
avg_volume, std_dev = estimate_ellipsoid_volume(M, N, a, b, c)

# Print the results
print(f"Average Ellipsoid Volume: {avg_volume}")
print(f"Standard Deviation: {std_dev}")
