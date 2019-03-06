class Employee:  # initialize a new class
    def __init__(self, name, employee_num, salary):
        self.name = name
        self.employee_num = employee_num
        self.salary = salary


class Supervisor(Employee):  # supervisor inherits the Employee class and then adds another data type
    def __init__(self, name, employee_num, salary, workers):
        super().__init__(name, employee_num, salary)  # takes info from the Employee class
        self.workers = workers  # defines new attribute


john = Supervisor("John", 20, 30, 1)
print(john.name)


class Animal:
    def __init__(self, blood, age, weight, height):
        self.blood = blood
        self.age = age
        self.weight = weight
        self.height = height


class Dog(Animal):
    def __init__(self, blood, age, weight, height, colour, hairOrFur):
        super().__init__(blood, age, weight, height)
        self. colour = colour
        self.hairOrFur = hairOrFur


class Labrador(Dog):
    def __init__(self, blood, age, weight, height, colour, hairOrFur, type):
        super().__init__(blood, age, weight, height, colour, hairOrFur)
        self.type = type


poochie = Dog("warm", 3, 100, 20, "golden", "fur", "cute")
print(poochie.type)

