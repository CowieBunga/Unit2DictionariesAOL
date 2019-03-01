'''
class Classroom:
    def __init__(self, numberOfStudents, numberOfDesks, course):
        self.numberOfStudents = numberOfStudents
        self.numberOfDesks = numberOfDesks
        self.course = course

room205 = Classroom(16,20,"ICS4U")
print(room205.course)
'''

'''
class School:
    def __init__(self, name, numOfStudents, yearsOld):
        self.name = name
        self.numOfStudents = numOfStudents
        self.yearsOld = yearsOld
Greenwood = School("Greenwood", 500, 16)
print("The name is", Greenwood.name, "it is", Greenwood.yearsOld, "years old", "It has", Greenwood.numOfStudents, "students")
'''

'''
class Car:
    def __init__(self, numOfDoors, brand):
        self.numOfDoors = numOfDoors
        self.brand = brand
        if numOfDoors == 2:
            self.type = "coupe"
        elif numOfDoors == 4:
            self.type = "sedan"
        else:
            self.type = "other"


car1 = Car(2, "toyota")
print(car1.type)
'''

class Universities:
    def __init__(self, SchoolName, numberOfStudents, address, mascot):
        self.programlist = []
        self.SchoolName = SchoolName
        self.numberOfStudents = numberOfStudents
        self.address = address
        self.mascot = mascot

    def addProgram(self, program):
        self.programlist.append(program)

    def __str__(self):
        output = ""
        for program in self.programlist:
            for student in program.studentList:
                output += student.name+" is in "+program.programName+" at "+self.SchoolName+"\n"
        return output

class Program:
    def __init__(self, programName, faculty, maxStudents):
        self.studentList = []
        self.programName = programName
        self.faculty = faculty
        self.maxStudents = maxStudents

    def addStudent(self, student):
        self.studentList.append(student)

class Student:
    def __init__(self, name, birthYear, originCity):
        self.name = name
        self.birthYear = birthYear
        self.originCity = originCity


Harvard = Universities("Harvard", 1000, "123 Boston", "Bulldog")

CompSci = Program("CompSci101", "Faculty of Compy", "10101")
Business = Program("Commerce", "Faculty of Commerce", "300000")

Dart = Student("Alex Dart", 2002, "YoMama")
Gomes = Student("Jeremy Gomes", 2002, "JeremyVille")
Cowie = Student("Jackson Cowie", 2002, "The Hospital")
Naprawa = Student("John Naprawa", 2002, "Women's College Hospital")

Harvard.addProgram(CompSci)
Harvard.addProgram(Business)

CompSci.addStudent(Dart)
CompSci.addStudent(Cowie)
Business.addStudent(Gomes)
Business.addStudent(Naprawa)


print(Harvard)