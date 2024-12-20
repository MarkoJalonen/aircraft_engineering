"""This module salculates the density at given height."""

from math import exp, pow
from constants import H_1, H_2, T_0, P_0, G_0, R, P_1, AIR_EXP
from temperature import temperature

def pressure(height: int) -> float:
    """Calculates the pressure at given height
    
    Args:
        height: The height at which the pressure should be 
                calculated in meters.

    Returns:
        The pressure at given height in Pa.

    Raises:
        ValueError: If 0 < height < 20000
    """

    p = 0
    match height:
        case 0:
            p = P_0
        case _ if 0 < height <= H_1:
            p = P_0 * pow((temperature(height) / T_0), AIR_EXP)
        case _ if 0 < H_1 < height <= H_2:
            p = P_1 * exp(-G_0 / (R * temperature(height)) * (height - H_1))
        case _:
            raise ValueError("Height must be between 0 and 20km!")
    return p

# Test routine
if __name__ == "__main__":
    print("h = 0 m -> p =", pressure(0))
    print("h = 7010 m -> p =", pressure(7010), "Pa")
    print("h = 11000 m -> p =", pressure(11000), "Pa")
    print("h = 11887 m -> p =", pressure(11887), "Pa")
    print("h = 19000 m -> p =", pressure(19000), "Pa")
    