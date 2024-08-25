#The follwing code is the study the motion of a simple pendulum and ultimately to plot its trajectory

# Importing the required libraries
import numpy as np
import matplotlib.pyplot as plt

# Defining the constants

g=9.81 #The value is in ms^-2
L=1.0 #The supposed length of the string
theta0 = np.pi/4 #This is the inital angle from whxich the bob was released
omega0 = 0.0 #The initial angular velocity of the bob
time_step=0.01 #The time step for the simulation
total_time=10.0 #The total time for which the simulation is to be run

#Creating the time array
t=np.arange(0,total_time,time_step)

#Creating arrays to store the values of the theta, omega, ke, pe, te
theta = np.zeros_like(t)
omega = np.zeros_like(t)
ke = np.zeros_like(t)
pe = np.zeros_like(t)
te = np.zeros_like(t)

#Setting the initial values
theta[0] = theta0
omega[0] = omega0

#Simulating the motion of the pendulm using the equations of motion

for i in range (1, len(t)):
    #Finding out the values of the angular accelaration
    alpha  = -g/L * np.sin(theta[i-1])

    #Finding out the new angular velocity and the new theta
    omega[i] = omega[i-1]+alpha * time_step
    theta[i] = theta[i-1]+omega[i] * time_step

    #Calcuting the KE, PE and TE
    ke[i] = 0.5 * L**2 * omega[i]**2
    pe[i] = 0.5 * g * L * (1-np.cos(theta[i]))
    te[i] = ke[i] + pe[i]

    #Converting the angles from degrees to radians
    theta_deg = np.degrees(theta)


    
#Plotting the trajectories

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, theta_deg, label='Angle (degrees)')
plt.xlabel('Time (s)')
plt.ylabel('Angle (degrees)')
plt.title('Simple Pendulum Motion')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t, ke, label='Kinetic Energy')
plt.plot(t, pe, label='Potential Energy')
plt.plot(t, te, label='Total Energy')
plt.xlabel('Time (s)')
plt.ylabel('Energy (Joules)')
plt.legend()
plt.title('Energy vs. Time')
plt.grid(True)

plt.tight_layout()
plt.show()
