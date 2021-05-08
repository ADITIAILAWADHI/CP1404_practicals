class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost
        self.age = 0
        self.vintage_string = ""
        guitar_age = self.get_age()
        if guitar_age >= 50:
            self.vintage_string = " (vintage)"

    def __str__(self):
        return "{:>10} ({}), worth ${:5,.2f}{}".format(self.name, self.year, self.cost, self.vintage_string)

    def get_age(self):
        self.age = 2021-self.year
        return self.age

    def is_vintage(self):
        x = self.get_age()
        if x >= 50:
            return True
        return False
