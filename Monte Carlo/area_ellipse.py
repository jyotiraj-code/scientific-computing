#Importing the dependencies
import numpy as np
import random

#Initializing the counter for points inside the ellipse

def estimate_ellipse_area(num_measurements, num_trials, semi_major_axis, semi_minor_axis):
    points_inside_ellipse=0

    for _ in range(num_trials):
        for _ in range(num_measurements):
            #Here we are generating random x and y values between -semi_major_axis and semi_major_axis
            x=random.uniform(-semi_major_axis, semi_major_axis)
            y=random.uniform(-semi_minor_axis, semi_minor_axis)

            #Checking if the point (x,y) is inside the ellipse using the ellipse equation
            if(x**2 / (semi_major_axis**2) + y**2 / (semi_minor_axis**2) <= 1):
                points_inside_ellipse+=1

    #Calculatng the estimated value of the area of the ellipse

    bounding_box_area=4*semi_major_axis*semi_minor_axis
    ellipse_area_estimate = bounding_box_area * (points_inside_ellipse / (num_measurements*num_trials))
    
    return ellipse_area_estimate

#Here is the input and details about the ellipse:

num_measurements=1000
num_trials=10000
semi_major_axis=3.0
semi_minor_axis=2.0

#Estimating the area and printing the results

ellipse_area_approximation = estimate_ellipse_area(num_measurements, num_trials, semi_major_axis, semi_minor_axis)


#True value of the area of the ellipse

true_ellipse_area = np.pi * semi_major_axis * semi_minor_axis

#Calculating the error percentage
relative_error_percentage = ((ellipse_area_approximation - true_ellipse_area)*100 / true_ellipse_area)

#Printing the results
print(f"The approximated area of the ellipse is: {ellipse_area_approximation}")
print(f"The true area of the ellipse is: {true_ellipse_area}")
print(f"The relative error percentage: {relative_error_percentage}")