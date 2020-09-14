class CovidData:

    def __init__(self, id, date, name, new_cases, total_cases, new_deaths, total_deaths):
        self.id = id
        self.date = date
        self.name = name
        self.new_cases = new_cases
        self.total_cases = total_cases
        self.new_deaths = new_deaths
        self.total_deaths = total_deaths

    def __str__(self):
        return str(self.id) +\
               " " + self.date + \
               " " + self.name + \
               " " + str(self.new_cases) + \
               " " + str(self.total_cases) + \
               " " + str(self.new_deaths) + \
               " " + str(self.total_deaths)
