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
    Dynamic Viscosity ($\mathrm{mu}$) measured in kg/m*s. Measures the fluids viscosity
    Specific heat capactiy (C) J/Kg*K. how much energy must be put in to heat up one kg of the fluid by one degree kelvin
Flow and geometric variables
    Fluid Density ($\mathrmP{Rho}$) Measured in Kg/m^3. Is a measure of how much mass is in each unit volume
    mean fluid velocity (V) measured in m/s. The average speed of all the fluid traveling down the pipe.
    Pipe diameter (D) Measured in M. The total length across the cross section of the pipe. 
Parts of the equation: 
    $\mathrm{Re}$ = $\mathrm{rho}$(V)(D)/$\mathrm{mu}$ 
    $\mathrm{Pr}$ = $\mathrm{mu}$ * C / K

    $\mathrm{Nu}$ = (h *D)/ K

Therefore, 

H = $$ \mathrm{Nu} = 0.023 \cdot \mathrm{Re}^{0.8} \cdot \mathr{Pr}^{0.4} $$ / D * K


##  Practical Real-World Workflow for an Engineer

1. Calculate $\mathrm{Re}$ using $V_m$ and $D$.
2. Calculate $\mathrm{Pr}$ using fluid properties.
3. Compute $\mathrm{Nu}$ via Dittus-Boelter.
4. Solve for $h = \frac{\mathrm{Nu} \cdot k}{D}$.
5. Plug $h$ into the exponential equation to find $T_{out}$.
6. Calculate $Q$ and verify if the [[Heat Exchanger]] meets the design load.
