from time import time
import numpy as np
import CoolProp.CoolProp as CP
#generate a normal distribution of temperatures
# 583.15 K is 310 C, 10 K is the standard deviation

number_of_data_points = 100000

def make_temperatures():
    temperatures = np.random.normal(583.15, 10, number_of_data_points)
    return temperatures

def make_parameters(temperatures):
    print(f"Generating {len(temperatures)} parameters")

    # Convert inputs to standard float lists/arrays if they are Pandas Series
    # CoolProp accepts arrays natively via PropsSI
    T_array = np.array(temperatures)

    # P is passed as a broadcasted constant array or scalar depending on interface
    P_val = 15.5 * 1e6  # CoolProp uses SI units (Pascals), so 15.5 MPa = 15.5 * 10^6 Pa

    # PropsSImulti handles vector inputs quickly across standard properties
    density = CP.PropsSI('D', 'T', T_array, 'P', P_val, 'Water')   # Density (kg/m3)
    specific_heat = CP.PropsSI('Cpmass', 'T', T_array, 'P', P_val, 'Water') # Cp (J/kg/K)
    dynamic_viscosity = CP.PropsSI('V', 'T', T_array, 'P', P_val, 'Water')  # Viscosity (Pa s)
    thermal_conductivity = CP.PropsSI('L', 'T', T_array, 'P', P_val, 'Water') # Conductivity (W/m/K)

    return density, specific_heat, dynamic_viscosity, thermal_conductivity

def make_diameters():
    diameters = np.random.uniform(0.50, 1.10, number_of_data_points)
    print(f"Generated {number_of_data_points} diameters")
    return diameters

def make_velocities():
    velocities = np.random.uniform(3.0, 16.0, number_of_data_points)
    print(f"Generated {number_of_data_points} velocities")
    return velocities

def generate_data(density, specific_heat, dynamic_viscosity, thermal_conductivity, diameters, velocities):
    # calculate the reynolds, prandtl, and nusselt numbers
    reynolds = (density * velocities * diameters) / dynamic_viscosity
    prandtl = (specific_heat * dynamic_viscosity) / thermal_conductivity
    nusselt = 0.023 * (reynolds ** 0.8) * (prandtl ** 0.3)
    #also need to calculate h using the nusselt number, is shown by nusselt * thermal_conductivity / diameter
    h = (nusselt * thermal_conductivity) / diameters
    print(f"Generated {number_of_data_points} reynolds, prandtl, nusselt, and h")
    return reynolds, prandtl, nusselt, h

def make_array(temperatures, density, specific_heat, dynamic_viscosity, 
thermal_conductivity, diameters, velocities, reynolds, prandtl, nusselt, h):
    # Shape: (1000, 11)
    array = np.column_stack((
        temperatures, density, specific_heat, dynamic_viscosity, 
        thermal_conductivity, diameters, velocities, reynolds, prandtl, nusselt, h
    ))
    print(f"Shape of array: {array.shape}")
    print(f"saved array to data/data.csv")
    return array

def create_synthetic_dataset():
    start_time = time()
    temperatures = make_temperatures()
    density, specific_heat, dynamic_viscosity, thermal_conductivity = make_parameters(temperatures)
    diameters = make_diameters()
    velocities = make_velocities()
    
    reynolds, prandtl, nusselt, h = generate_data(
        density, specific_heat, dynamic_viscosity, 
        thermal_conductivity, diameters, velocities
    )
    
    array = make_array(
        temperatures, density, specific_heat, dynamic_viscosity, 
        thermal_conductivity, diameters, velocities, reynolds, prandtl, nusselt, h
    )
    
    np.savetxt('data/data.csv', array, delimiter=',', header="temp,rho,cp,mu,k,diameter,velocity,Re,Pr,Nu,h", comments='')
    end_time = time()

    # Calculate and print the elapsed time
    execution_time = end_time - start_time
    print(f"Program completed in {execution_time:.1f} seconds.")

    #may potentially want to implement a CLI later for the program to make it more user friendly

if __name__ == "__main__":
    create_synthetic_dataset()
