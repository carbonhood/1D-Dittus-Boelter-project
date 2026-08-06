import numpy as np
from iapws import IAPWS97

#generate a normal distribution of temperatures
# 583.15 K is 310 C, 10 K is the standard deviation

def make_temperatures():
    temperatures = np.random.normal(583.15, 10, 1000)
    return temperatures

def make_parameters(temperatures):
    density = []
    specific_heat = []
    dynamic_viscosity = []
    thermal_conductivity = []
    
    for temperature in temperatures:
        #use the iapws library to generate the parameters
        water = IAPWS97(T=temperature, P=15.5)
        density.append(water.rho)
        specific_heat.append(water.cp)
        dynamic_viscosity.append(water.mu)
        thermal_conductivity.append(water.k)
        
    # Convert lists to NumPy arrays for element-wise math down the line
    return (np.array(density), np.array(specific_heat), 
            np.array(dynamic_viscosity), np.array(thermal_conductivity))

def make_diameters():
    diameters = np.random.uniform(0.50, 1.10, 1000)
    return diameters

def make_velocities():
    velocities = np.random.uniform(3.0, 16.0, 1000)
    return velocities

def generate_data(density, specific_heat, dynamic_viscosity, thermal_conductivity, diameters, velocities):
    # calculate the reynolds, prandtl, and nusselt numbers
    reynolds = (density * velocities * diameters) / dynamic_viscosity
    prandtl = (specific_heat * dynamic_viscosity) / thermal_conductivity
    nusselt = 0.023 * (reynolds ** 0.8) * (prandtl ** 0.4)
    #also need to calculate h using the nusselt number, is shown by nusselt * thermal_conductivity / diameter
    h = (nusselt * thermal_conductivity) / diameters
    return reynolds, prandtl, nusselt, h

def make_array(temperatures, density, specific_heat, dynamic_viscosity, 
thermal_conductivity, diameters, velocities, reynolds, prandtl, nusselt, h):
    # Shape: (1000, 11)
    array = np.column_stack((
        temperatures, density, specific_heat, dynamic_viscosity, 
        thermal_conductivity, diameters, velocities, reynolds, prandtl, nusselt, h
    ))
    return array

if __name__ == "__main__":
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
