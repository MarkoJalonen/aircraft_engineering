from constants import Constants

H_1 = Constants.H_1.value
H_2 = Constants.H_2.value
T_0 = Constants.T_0.value
P_0 = Constants.P_0.value
L_0 = Constants.L_0.value

def temperature(height):
    T = 0
    match height:
        case 0: 
            T = T_0
        case _ if 0 < height <= H_1:
            T = T_0 + L_0 * height
        case _ if 0 < H_1 < height <= H_2:
            T = 216.69
        case _:
            raise ValueError("Height must be between 0 and 20km!")
    return T

# Test routine
if __name__ == "__main__":
    print("h = 0 -> T =", temperature(0), "{:.2f}".format(temperature(0) - 273.15))
    print("h = 1219 -> T =", temperature(1219), "{:.2f}".format(temperature(1219) - 273.15))
    print("h = 7010 -> T =", temperature(7010), "{:.2f}".format(temperature(7010) - 273.15))
    print("h = 11887 -> T =", temperature(11887), "{:.2f}".format(temperature(11887) - 273.15))
    print("h = 19000 -> T =", temperature(19000), "{:.2f}".format(temperature(19000) - 273.15))
    print("h = 22000", temperature(22000))
    print("h = -42", temperature(-42))

