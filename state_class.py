import csv
import matplotlib.pyplot as plt

filename = 'state_crime.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    states = []
    for row in reader:
        if row[0] not in states:
            states.append(row[0])

class State:
    def __init__(self, name):
        if name in states:
            self.name = name
        else:
            print(f'You entered {name}. That is not in the state list.')
        self.year = self.getYear()
        self.population = self.getPopulation()
        #Property theft rates
        self.allProperty = self.getAllProperty()
        self.burglary = self.getBurglary()
        self.larceny = self.getLarceny()
        self.motor = self.getMotor()
        #Violent crime rates
        self.allViolent = self.getAllViolent()
        self.assault = self.getAssault()
        self.murder = self.getMurder()
        self.rape = self.getRape()
        self.robbery = self.getRobbery()
        #Total Crime

    def plot(self, stateCrime, title, ylabel):
        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(self.year, stateCrime)

        ax.set_title(f'{title}', fontsize=20)
        ax.set_xlabel("Year from 1960 to 2019")
        ax.set_ylabel(f'{ylabel}')

        plt.show()

    def getPopulation(self):
        with open(filename) as f:
            reader = csv.reader(f)
            population = []
            for row in reader:
                if row[0] == self.name:
                    population.append(int(row[2]))
        return population

    def getYear(self):
        with open(filename) as f:
            reader = csv.reader(f)
            year = []
            for row in reader:
                if row[0] == self.name:
                    year.append(int(row[1]))
        return year

    def getAllProperty(self):
        with open(filename) as f:
            reader = csv.reader(f)
            allProperty = []
            for row in reader:
                if row[0] == self.name:
                    allProperty.append(float(row[3]))
        return allProperty

    def getBurglary(self):
        with open(filename) as f:
            reader = csv.reader(f)
            burglary = []
            for row in reader:
                if row[0] == self.name:
                    burglary.append(float(row[4]))
        return burglary

    def getLarceny(self):
        with open(filename) as f:
            reader = csv.reader(f)
            larceny = []
            for row in reader:
                if row[0] == self.name:
                    larceny.append(float(row[5]))
        return larceny

    def getMotor(self):
        with open(filename) as f:
            reader = csv.reader(f)
            motor = []
            for row in reader:
                if row[0] == self.name:
                    motor.append(float(row[6]))
        return motor

    def getAllViolent(self):
        with open(filename) as f:
            reader = csv.reader(f)
            allViolent = []
            for row in reader:
                if row[0] == self.name:
                    allViolent.append(float(row[7]))
        return allViolent

    def getAssault(self):
        with open(filename) as f:
            reader = csv.reader(f)
            assault = []
            for row in reader:
                if row[0] == self.name:
                    assault.append(float(row[8]))
        return assault

    def getMurder(self):
        with open(filename) as f:
            reader = csv.reader(f)
            murder = []
            for row in reader:
                if row[0] == self.name:
                    murder.append(float(row[9]))
        return murder

    def getRape(self):
        with open(filename) as f:
            reader = csv.reader(f)
            rape = []
            for row in reader:
                if row[0] == self.name:
                    rape.append(float(row[10]))
        return rape

    def getRobbery(self):
        with open(filename) as f:
            reader = csv.reader(f)
            robbery = []
            for row in reader:
                if row[0] == self.name:
                    robbery.append(float(row[11]))
        return robbery


#I'm sure there is a way to automatically do this, but I am new.
United_States = State('United States')
Texas = State('Texas')

Alabama = State('Alabama')
Alaska = State('Alaska')
Arizona = State('Arizona')
Arkansas = State('Arkansas')

California = State('California')
Colorado = State('Colorado')
Connecticut = State('Connecticut')

Delaware = State('Delaware')
District_of_Columbia = State('District of Columbia')

Florida = State('Florida')

Georgia = State('Georgia')

Hawaii = State('Hawaii')

Idaho = State('Idaho')
Illinois = State('Illinois')
Indiana = State('Indiana')
Iowa = State('Iowa')

Kansas = State('Kansas')
Kentucky = State('Kentucky')

Louisiana = State('Louisiana')

Maine = State('Maine')
Maryland = State('Maryland')
Massachusetts = State('Massachusetts')
Michigan = State('Michigan')
Minnesota = State('Minnesota')
Mississippi = State('Mississippi')
Missouri = State('Missouri')
Montana = State('Montana')

Nebraska = State('Nebraska')
Nevada = State('Nevada')
New_Hampshire = State('New Hampshire')
New_Jersey = State('New Jersey')
New_Mexico = State('New Mexico')
New_York = State('New York')
North_Carolina = State('North Carolina')
North_Dakota = State('North Dakota')

Ohio = State('Ohio')
Oklahoma = State('Oklahoma')
Oregon = State('Oregon')

Pennsylvania = State('Pennsylvania')

Rhode_Island = State('Rhode Island')

South_Carolina = State('South Carolina')
South_Dakota = State('South Dakota')

Tennessee = State('Tennessee')
#Texas already done

#United States already done
Utah = State('Utah')

Vermont = State('Vermont')
Virginia = State('Virginia')

Washington = State('Washington')
West_Virginia = State('West Virginia')
Wisconsin = State('Wisconsin')
Wyoming = State('Wyoming')

