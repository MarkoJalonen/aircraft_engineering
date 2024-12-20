"""File containing constants for the atmosphere.

These are used to calculate the different qualities of atmosphere
at different heights. 
"""

R: float = 287.04              # J/K⋅kg
L_0: float = -0.0065           # K/m
T_0: float = 288.15            # K
P_0: float = 101325.0          # N/m²
P_1: float = 22653.0           # N/m²
G_0: float = 9.81              # m/s²
RHO_0: float = 1.225           # kg/m³
RHO_1: float = 0.3639          # kg/m³
H_1: float = 11000.0           # m
H_2: float = 20000.0           # m
AIR_EXP: float = 5.26          # g_0 / LR, no unit
