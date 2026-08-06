import numpy
import iapws
from iapws import IAPWS97

#reactor operates at an average of 583.15 K, in a normal distrubition
#sigma of 10K
#generate 1000 temperatures

temperatures = numpy.random.normal(583.15, 10, 1000)

def make_parameters(temperatures):
    density = []
    specific_heat = []
    dynamic_viscosity = []
    thermal_conductivity = []

    for temperature in temperatures:
        #use the iapws library to find the parameters at each temperature, with a pressure of 155 bar
        water = iapws.IAPWS97(T=temperature, P=15.5)
        density.append(water.rho)
        specific_heat.append(water.cp)
        dynamic_viscosity.append(water.mu)
        thermal_conductivity.append(water.k)
    #return as a numpy array of parameters at each temperature
    parameters = numpy.array([density, specific_heat, dynamic_viscosity, thermal_conductivity])   
    parameters = numpy.column_stack((density, specific_heat, dynamic_viscosity, thermal_conductivity))
    return parameters
def make_diameters():
    diameters = numpy.random.uniform(.50, 1.10, 1000)
    return diameters

def make_velocities():
    velocities = numpy.random.uniform(3.0, 16.0, 1000)
    return velocities

def make_array(parameters, diameters, velocities):
    array = numpy.array([parameters, diameters, velocities])
    array = numpy.column_stack((parameters, diameters, velocities))
    return array

def generate_data(temperature_list, diameter_list, velocity_list):
    #Calculate the reynolds number, prandtl number, and nusselt number for 1000 zip combination of temperature, diameter, and velocity
    #convert to pandas dataframe and save to a csv file in data folder
    #return the dataframe
    pass

#run the script from a main file, maybe a command line interface
if __name__ == "__main__":
    parameters = make_parameters(temperatures)
    diameters = make_diameters()
    velocities = make_velocities()
    array = make_array(parameters, diameters, velocities)
    print(array.shape)