from constants import H_1, H_2, T_0, P_0, L_0

def temperature(height: int) -> float:
    """Calculates the temperature at given height
    
    Args:
        height: The height at which the temperature should be 
                calculated in meters.

    Returns:
        The temperature at given height in celcius.

    Raises:
        ValueError: If 0 < height < 20000
    """

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
    print("h = 0 -> T =", temperature(0), temperature(0) - 273.15)
    print("h = 1219 -> T =", temperature(1219), temperature(1219) - 273.15)
    print("h = 7010 -> T =", temperature(7010), temperature(7010) - 273.15)
    print("h = 11887 -> T =", temperature(11887), temperature(11887) - 273.15)
    print("h = 19000 -> T =", temperature(19000), temperature(19000) - 273.15)
    print("h = 22000", temperature(22000), temperature(22000 - 273.15))
    print("h = -42", temperature(-42), temperature(-42 - 273.15))