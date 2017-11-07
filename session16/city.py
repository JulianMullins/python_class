class City:

    def __init__(self, arg_name="Unknown", pop = 0, gdp = 0):
        self.name = arg_name
        self.population = pop
        self.gdp = gdp

    def __str__(self):
        return '{} has {} people, with gdp per capita of {}.'.format(self.name, self.population, self.gdp)

    def __gt__(self, another_city):
        if self.gdp > another_city.gdp:
            return True
        elif self.gdp == another_city.gdp:
            if self.population > another_city.population:
                return True
        return False

    def __add__(self, another_city):
        city = City()
        city = self.name + another_city.name
        city = self.population + another_city.population
        city = (self.gdp + another_city.gdp)/2
        return city

city1 = City()

print(city1.name, city1.population)

new_york = City("New York", 8500000, 75000)
print(new_york)

boston = City('Boston', 600000, 75000)
print(boston)

print(new_york>boston)