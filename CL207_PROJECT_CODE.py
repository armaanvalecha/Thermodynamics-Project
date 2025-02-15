import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Constants
R = 8.314  # Ideal gas constant in J/(mol·K)

# Assumed parameters
T_min = 273  # Minimum temperature in Kelvin
T_max = 1500  # Maximum temperature in Kelvin
P_min = 1e5  # Minimum pressure in Pascals
P_max = 2e6  # Maximum pressure in Pascals

# Constants for Cp calculation (from Sandler data or assumed)
A = 10.046       # Constant A for Cp in J/(mol·K)
B = 17.866     # Constant B for Cp
C = -11.511      # Constant C for Cp
D = 28.439   # Constant D for Cp

# Define Cp as a function of temperature based on provided constants
def Cp(T):
    return A + B * T**1 * 1e-2 + C * T**2 * 1e-5 + D * T**3 * 1e-9

# Ideal gas enthalpy and entropy calculations
def enthalpy(T):
    Cp_integral, _ = quad(lambda t: Cp(t), 298, T)
    return Cp_integral  # J/mol (assuming enthalpy at 298 K is zero for simplicity)

def entropy(T):
    S_integral, _ = quad(lambda t: Cp(t) / t, 298, T)
    return S_integral  # J/(mol·K) (assuming entropy at 298 K is zero for simplicity)

# Ideal gas volume calculation based on PV = nRT
def volume(T, P):
    return R * T / P  # Ideal gas law

# Generate thermodynamic property plots and calculate values
def plot_properties():
    T_vals = np.linspace(T_min, T_max, 100)
    P_vals = np.linspace(P_min, P_max, 100)

    # Calculate Cp, H, and S for the temperature range
    Cp_values = [Cp(T) for T in T_vals]
    H_values = [enthalpy(T) for T in T_vals]
    S_values = [entropy(T) for T in T_vals]
    
    # Print the calculated values for Cp, H, and S at different T values
    print(f"{'T (K)':<10}{'Cp (J/(mol·K))':<20}{'H (J/mol)':<20}{'S (J/(mol·K))':<20}")
    print("="*70)
    for T, cp, h, s in zip(T_vals, Cp_values, H_values, S_values):
        print(f"{T:<10.1f}{cp:<20.2f}{h:<20.2f}{s:<20.2f}")

    # Cp vs. T
    plt.figure()
    plt.plot(T_vals, Cp_values, label="Cp vs T")
    plt.xlabel("Temperature (K)")
    plt.ylabel("Molar Heat Capacity, Cp (J/(mol·K))")
    plt.title("Cp vs. Temperature")
    plt.grid(True)
    plt.legend()
    plt.show()

    # P-V Plot (ideal gas behavior, hyperbolic relationship)
    plt.figure()
    for T in [T_min, (T_min + T_max) / 2, T_max]:  # Example: plots at three different temperatures
        V_vals = [volume(T, P) for P in P_vals]
        plt.plot(V_vals, P_vals, label=f"P-V Curve at T={T} K")
    
    plt.xlabel("Volume (m^3/mol)")
    plt.ylabel("Pressure (Pa)")
    plt.title("Pressure-Volume (P-V) Plot (Ideal Gas Behavior)")
    plt.grid(True)
    plt.legend()
    plt.show()

    # P-H Plot (Pressure vs Enthalpy)
    plt.figure()
    plt.plot(H_values, P_vals, label="P-H Curve")
    plt.xlabel("Enthalpy (J/mol)")
    plt.ylabel("Pressure (Pa)")
    plt.title("Pressure-Enthalpy (P-H) Plot")
    plt.grid(True)
    plt.legend()
    plt.show()

    # T-S Plot (Temperature vs Entropy)
    plt.figure()
    plt.plot(T_vals, S_values, label="T-S Curve")
    plt.xlabel("Temperature (K)")
    plt.ylabel("Entropy (J/(mol·K))")
    plt.title("Temperature-Entropy (T-S) Plot")
    plt.grid(True)
    plt.legend()
    plt.show()

# Run the plotting function
plot_properties()