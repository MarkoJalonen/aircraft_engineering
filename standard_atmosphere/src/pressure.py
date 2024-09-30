from constants import Constants
from math import exp, pow
from temperature import temperature

H_1 = Constants.H_1.value
H_2 = Constants.H_2.value
T_0 = Constants.T_0.value
P_0 = Constants.P_0.value
G_0 = Constants.G_0.value
R = Constants.R.value
P_1 = Constants.P_1.value
AIR_EXP = Constants.AIR_EXP.value

def pressure(height: int) -> float:
    p = 0
    match height:
        case 0: 
            p = P_0
        case _ if 0 < height <= H_1:
            p = P_0 * pow((temperature(height)/T_0), AIR_EXP)
        case _ if 0 < H_1 < height <= H_2:
            p = P_1 * exp(-G_0/(R*temperature(height))*(height-H_1))
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
    