A collection of modules that calculate temperature, density or pressure
of the atmosphere given the geopotential altitude.

These modules are found in the ./src folder.

The ./src/print_csv.py script will generate a table with rows of aforementioned
data. This table will be stored in .printouts/ folder. To run this script,
call "$ python3 print_csv.py <altitude>". The data will be calculated in
100 meter intervals for the next 3000 meters from the given starting altitude.
The given altitude should be an interger between 0 and 17000 meters.

Written with Python 3.11.2.