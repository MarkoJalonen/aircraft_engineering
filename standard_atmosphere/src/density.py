from constants import H_1, H_2, T_0, G_0, R, RHO_0, RHO_1, AIR_EXP
from math import exp, pow
from temperature import temperature

def density(height: int) -> float:
    """Calculates the density at given height
    
    Args:
        height: The height at which the density should be 
                calculated in meters.

    Returns:
        The density at given height in kg/m³.

    Raises:
        ValueError: If 0 < height < 20000
    """

    rho = 0
    match height:
        case 0: 
            rho = RHO_0
        case _ if 0 < height <= H_1:
            rho = RHO_0 * pow((temperature(height) / T_0), AIR_EXP - 1)
        case _ if 0 < H_1 < height <= H_2:
            rho = RHO_1 * exp(-G_0 / (R * temperature(height)) * (height - H_1))
        case _:
            raise ValueError("Height must be between 0 and 20km!")
    return rho

# Test routine
if __name__ == "__main__":
    print("h = 0 m -> rho =", density(0), "kg/m³")
    print("h = 7010 m -> rho =", density(7010), "kg/m³")
    print("h = 11000 m -> rho =", density(11000), "kg/m³")
    print("h = 11887 m -> rho =", density(11887), "kg/m³")
    print("h = 19000 m -> rho =", density(19000), "kg/m³")
    