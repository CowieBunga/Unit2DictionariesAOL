'''
class Classroom:
    def __init__(self, numberOfStudents, numberOfDesks, course):
        self.numberOfStudents = numberOfStudents
        self.numberOfDesks = numberOfDesks
        self.course = course

room205 = Classroom(16,20,"ICS4U")
print(room205.course)
'''

class School:
    def __init__(self, name, numOfStudents, yearsOld):
        self.name = name
        self.numOfStudents = numOfStudents
        self.yearsOld = yearsOld
Greenwood = School("Greenwood", 500, 16)
print("The name is", Greenwood.name, "it is", Greenwood.yearsOld, "years old", "It has", Greenwood.numOfStudents, "students")

class Car:
    def __init__(self, numOfDoors, brand):
        self.numOfDoors = numOfDoors
        self.brand = brand


coupe = Car(2, "BMW")
sedan = Car(4, "Honda")

print("The", coupe.brand, "has", coupe.numOfDoors, "doors")
print("The", sedan.brand, "has", sedan.numOfDoors, "doors")
