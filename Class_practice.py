class Person:
    def __init__(self, full_name=None, year_b=1990):
        self.full_name = full_name
        self.year_b = year_b
        self.name = full_name.split(' ')[0]
        self.surname = full_name.split(' ')[1]
        self.age_in = 2019 - year_b

    # def set_name(self, name):
    #     self.name = name


p = Person('Nika Andreeva', 1991)
print(p.name)
print(p.surname)
print(p.age_in)
# p2 = Person('Vasya')
# print(p2.name)

class Employee(Person):
    def __init__(self, full_name=None, year_b=1990, position=None, exp=0, salary=0):
        super().__init__(full_name, year_b)
        self.position = position
        self.exp = exp
        self.salary = salary

    def income(self, plus=0):
        return self.salary + plus

    def prefix(self, position, exp):
        if exp < 2:
            self.prefix = "Junior" + " " + position
        elif 2 < exp < 4:
            self.prefix = "Middle" + " " + position
        else:
            self.prefix = "Senior" + " " + position
        return self.prefix

p1 = Person("Nika Andreeva", 1991, 'programmer')
print(p1.prefix)
