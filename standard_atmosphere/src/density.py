from constants import Constants
from math import exp, pow
from temperature import temperature

H_1 = Constants.H_1.value
H_2 = Constants.H_2.value
T_0 = Constants.T_0.value
G_0 = Constants.G_0.value
R = Constants.R.value
RHO_0 = Constants.RHO_0.value
RHO_1 = Constants.RHO_1.value
AIR_EXP = Constants.AIR_EXP.value

def density(height: int) -> float:
    rho = 0
    match height:
        case 0: 
            rho = RHO_0
        case _ if 0 < height <= H_1:
            rho = RHO_0 * pow((temperature(height)/T_0), AIR_EXP - 1)
        case _ if 0 < H_1 < height <= H_2:
            rho = RHO_1 * exp(-G_0/(R*temperature(height))*(height-H_1))
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
    