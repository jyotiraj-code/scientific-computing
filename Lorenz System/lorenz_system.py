#This is the code to simulate the Lorenz Systsm to show the Chaos theory in action

#First we import the necessary libraries
import matplotlib.pyplot as plt
#First defining the paramenters for the Lorenz System

sigma=10.0
rho=28.0
beta=8.0/3.0

#Suppose the inital conditions are as such
x,y,z = 0.0,1.0,0.0

#Now we define the time step and the number of iterations

dt=0.01 #This is the value of the time setp
num_setps=5000 #This is the number of iterations or steps

#Now we define the arrays to store the values of x,y and z
x_values,y_values,z_values=[],[],[]

#Now performing the iterations

for i in range(num_setps):
    x_values.append(x)
    y_values.append(y)
    z_values.append(z)
    
    #Now we define the values of dx,dy and dz
    dx=(sigma*(y-x))*dt
    dy=(x*(rho-z)-y)*dt
    dz=(x*y-beta*z)*dt
    
    #Now we update the values of x,y and z
    x+=dx
    y+=dy
    z+=dz

    #Writing a text based visualization of the Lorenz System (i.e priting the coordinates)
    print(f"Step {i}: x = {x_values[i]:.2f}, y = {y_values[i]:.2f}, z = {z_values[i]:.2f}")

#Now we plot the values of x,y and z and showing the butterfly effect pattern

plt.figure(figsize=(10, 6))
plt.plot(x_values, z_values, lw=0.5)
plt.xlabel("X")
plt.ylabel("Z")
plt.title("Lorenz System Butterfly Effect")
plt.show()