'''Alex Brittain's State Crime Data Visualization
CSV file obtained from
https://corgis-edu.github.io/corgis/csv/state_crime/
based on fbi reports
https://ucr.fbi.gov/crime-in-the-u.s/2019/crime-in-the-u.s.-2019/downloads/download-printable-files
'''
from state_class import *

def main():
    '''Instructions for use:
The state_class.py file has the methods for reading the csv file and storing the data in lists.
I manually instantiated all of the states. Surely, there is a better way to do that, but this is my first time doing this.

#data

To make a plot use, state_name.plot(state_name.crime, 'Title', 'ylabel')
    '''
    United_States.plot(United_States.allViolent,'United States Violent Crimes', 'Violent crimes per 100,000')
    # Alaska.plot(Alaska.motor, 'Alaskan Motor Crime Rates', 'Crimes per 100,000')


# If the program is run (instead of imported), run:
if __name__ == '__main__':
    main()