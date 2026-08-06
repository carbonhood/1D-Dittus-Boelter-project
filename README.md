# 1D-Dittus-Boelter-project
Making an engineering based project to help me learn python and data science as a mechanical engineer. The Dittus-Boelter equations basically tell the extra amount of cooling that come from varying the speed of a liquid in a pipe.

Basic Variables and Constants

| **Nusselt Number**  | $\mathrm{Nu}$ | "How much better does moving liquid carry heat compared to just sitting still?" (We solve for this). |
| :------------------ | :------------ | :--------------------------------------------------------------------------------------------------- |
| **Reynolds Number** | $\mathrm{Re}$ | "How much swirling vs. smooth sliding is happening?" Bigger = more chaotic mixing.                   |
| **Prandtl Number**  | $\mathrm{Pr}$ | "Does this fluid spread heat easily (water) or hoard it (oil)?"                                      |

$$ \mathrm{Nu} = 0.023 \cdot \mathrm{Re}^{0.8} \cdot \mathrm{Pr}^{0.4} $$

##  Practical Real-World Workflow for an Engineer

1. Calculate $\mathrm{Re}$ using $V_m$ and $D$.
2. Calculate $\mathrm{Pr}$ using fluid properties.
3. Compute $\mathrm{Nu}$ via Dittus-Boelter.
4. Solve for $h = \frac{\mathrm{Nu} \cdot k}{D}$.
5. Plug $h$ into the exponential equation to find $T_{out}$.
6. Calculate $Q$ and verify if the [[Heat Exchanger]] meets the design load.
