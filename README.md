# 1D-Dittus-Boelter-project
Making an engineering based project to help me learn python and data science as a mechanical engineer. The Dittus-Boelter equations basically tell the extra amount of cooling that come from varying the speed of a liquid in a pipe.

Basic Variables and Constants

| **Nusselt Number**  | $\mathrm{Nu}$ | "How much better does moving liquid carry heat compared to just sitting still?" (We solve for this). |
| :------------------ | :------------ | :--------------------------------------------------------------------------------------------------- |
| **Reynolds Number** | $\mathrm{Re}$ | "How much swirling vs. smooth sliding is happening?" Bigger = more chaotic mixing.                   | 
| **Prandtl Number**  | $\mathrm{Pr}$ | "Does this fluid spread heat easily (water) or hoard it (oil)?"                                      |

$$ \mathrm{Nu} = 0.023 \cdot \mathrm{Re}^{0.8} \cdot \mathrm{Pr}^{0.4} $$

h: Convective heat transfer coefficient W/m^2 (Output variable) Rate of heat transfer between the fluid and pipe wall

Fluid Transport variables;

    Thermal Conductivity (K): measured in W/(m*K) How easily the fluid itself conducts heat. (watts per meter kelvin)

    Dynamic Viscosity (μ) measured in kg/m*s. Measures the fluids viscosity

    Specific heat capactiy (C) J/Kg*K. how much energy must be put in to heat up one kg of the fluid by one degree kelvin

Flow and geometric variables

    Fluid Density  Measured(ρ) in Kg/m^3. Is a measure of how much mass is in each unit volume

    mean fluid velocity (V) measured in m/s. The average speed of all the fluid traveling down the pipe.

    Pipe diameter (D) Measured in M. The total length across the cross section of the pipe. 

Parts of the equation: 

$$ \mathrm{Re} = \frac{\rho V D}{\mu} $$

$$ \mathrm{Pr} = \frac{\mu C_p}{k} $$

$$ \mathrm{Nu} = \frac{h D}{k} $$


Therefore, 

$$ H = \frac{\mathrm{Nu} \cdot K}{D} = \frac{0.023 \cdot \mathrm{Re}^{0.8} \cdot \mathrm{Pr}^{0.4} \cdot K}{D} $$

Inputs to vary for data: Density, Diameter, Mean fluid velocity
Specific Heat, Thermal conductivity, Dynamic Viscosity

##  Practical Real-World Workflow for an Engineer

1. Calculate $\mathrm{Re}$ using $V_m$ and $D$.
2. Calculate $\mathrm{Pr}$ using fluid properties.
3. Compute $\mathrm{Nu}$ via Dittus-Boelter.
4. Solve for $h = \frac{\mathrm{Nu} \cdot k}{D}$.
5. Plug $h$ into the exponential equation to find $T_{out}$.
6. Calculate $Q$ and verify if the [[Heat Exchanger]] meets the design load.

## Data Generation

The data generation module works by first generating a normal distribution of water temperatures often seen in a nuclear reactor, assumed to be at 155 bar. 

The file then uses the IAPWS library (stands for International Agency Protection of Water Streams or something like that idek) to generate values for density, specific heat, thermal conductivity, and dynamic viscosity at 1000 different temperature values

Next, it generates 1000 normal velocities and 1000 uniform diameters

After this, we plug our values into the equation and make out re, pr, and Nu, and h using our data for each data point in the array.

then we output to the data.csv file

I decided to use Coolprop because it can already do the vectorized math (whatever that means), instead of IAPWS library. Making that small change took prgram runtime from 25.0 seconds on average to 5.0 seconds on average

## Making the machine learning algorithm

Based on my understanding, a machine learning model is a function that takes in multiple inputs and predicts an output using a neural network. We are going to have 7 input parameters temperatures, density, specific_heat, dynamic_viscosity, 
thermal_conductivity, diameters, velocities,

Then the function has weights that it applies to the inputs, and all of the nuerons, and it links the nuerons itself. 

I am going to try using 2 hidden layers, the first with 64 nuerons, the second with 32, and the input layer with 7 inputs, and an output layer with 1 output (h)

I am avoiding using the reynolds, nusselt, and prandtl numbers to hopefully avoid the program overfitting to dividing the prandtl by K/d, so that we can actually ask about things like changes to velocity, temperature, and diameter.

To set up the nueral network, we for numpy load the data set from the csv file, and then we split the data into 80% train and 20% test. 

I looked up online a lot of how to set up the neural network, but it seems to be pretty standardized across the web and it works so we roll with it.


