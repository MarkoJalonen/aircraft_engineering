from temperature import temperature
from pressure import pressure
from density import density
import csv
import sys

def print_csv(start_h: int) -> None:
    csv_file = open("../printouts/standard_atmosphere_table.csv", "w", newline="")
    try:
        writer = csv.writer(csv_file)
        field = ["geopotential height [m]", "pressure [N/m²]", "abs. temperature [K]", "density [kg/m³]"]

        writer.writerow(field)
        h = start_h
        while h <= start_h + 3000:
            data = [h, pressure(h), temperature(h), density(h)]
            writer.writerow(data)
            h += 100
    except ValueError:
        print("Start height not between 0 and 17000!")
    except IOError:
        print("Could not write to or create a file in '../printouts'!")
    finally:
        csv_file.close()

if __name__ == "__main__":
    try:
        print_csv(int(sys.argv[1]))
    except IndexError:
        print("Give a starting height in meters between 0 and 17000 as an argument.")
