import numpy as np
import matplotlib.pyplot as plt

# Constants
hbar = 1.0  # Reduced Planck's constant
mass = 1.0  # Mass of the particle
omega = 1.0  # Angular frequency of the harmonic oscillator

# Potential energy function for the harmonic oscillator
def potential_energy(x):
    return 0.5 * mass * omega**2 * x**2

# Time-independent Schrödinger Equation (TISE) for the harmonic oscillator
def schrodinger_eqn(Phi, x, E):
    Phi_prime = np.zeros_like(Phi, dtype=complex)
    V = potential_energy(x)
    
    # Parity choice: Even
    if np.real(Phi[0]) % 2 == 0:
        Phi_prime[0] = 0
        Phi_prime[1] = 1.0
        
    # Parity choice: Odd
    else:
        Phi_prime[0] = 1.0
        Phi_prime[1] = 0

    for i in range(2, len(x)):
        k1 = hbar / (2.0 * mass) * (np.abs(Phi_prime[i - 1])**2 - (E - V[i - 1]) * np.abs(Phi[i - 1])**2)
        k2 = hbar / (2.0 * mass) * (np.abs(Phi_prime[i - 1] + 0.5 * hbar * k1 / np.abs(Phi[i - 1]))**2 - (E - V[i - 1] - 0.5 * hbar * k1 / np.abs(Phi[i - 1])) * np.abs(Phi[i - 1])**2)
        k3 = hbar / (2.0 * mass) * (np.abs(Phi_prime[i - 1] + 0.5 * hbar * k2 / np.abs(Phi[i - 1]))**2 - (E - V[i - 1] - 0.5 * hbar * k2 / np.abs(Phi[i - 1])) * np.abs(Phi[i - 1])**2)
        k4 = hbar / (2.0 * mass) * (np.abs(Phi_prime[i - 1] + hbar * k3 / np.abs(Phi[i - 1]))**2 - (E - V[i - 1] - hbar * k3 / np.abs(Phi[i - 1])) * np.abs(Phi[i - 1])**2)
        Phi_prime[i] = Phi_prime[i - 1] + hbar / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)
        Phi[i] = Phi[i - 1] + hbar / 6.0 * (Phi_prime[i - 1] + 2 * Phi_prime[i - 1] + 2 * Phi_prime[i - 1] + Phi_prime[i - 1])
        
        # Normalize the wavefunction at each step
        norm = np.sqrt(np.trapz(np.abs(Phi)**2, x))
        Phi /= norm

    return Phi

# Define the range for x
x_min = -2.0
x_max = 2.0
x_num_points = 200
x = np.linspace(x_min, x_max, x_num_points)

# Energy step size
h = 0.05


# Choose trial energies
energies = [0.5, 1.5, 2.5]


# Initialize the wavefunction and its derivative
Phi0 = np.zeros_like(x, dtype=complex)
Phi0[0] = 1.0  # Initial value of the wavefunction
Phi0[1] = 1.0 + h  # Initial value of the derivative (parity dependent)

# Main loop for different trial energies
for E in energies:
    Phi = schrodinger_eqn(Phi0, x, E)
    
    # Plot the wavefunction
    plt.figure()
    plt.plot(x, np.abs(Phi)**2)
    plt.xlabel('Position (x)')
    plt.ylabel('Probability Density')
    plt.title(f'Wavefunction for E = {E}')
    plt.grid(True)
    plt.show()
