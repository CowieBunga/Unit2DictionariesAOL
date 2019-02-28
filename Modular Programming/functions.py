import csv
def returnOdd(list1):
    holder = []
    for i in range(len(list1)):
        if i%2 == 1:
            holder.append(list1[i])
    return holder

def csvTo2DList(database):
    read = csv.reader(database)
    data = [row for row in read]
    return data

def specialInput(data):
    firstname = input("Fisrt Name: ").title()
    for item in data:
        if firstname in item:
            return str(firstname)

def listQuery(data, firstname):
    for i in range(len(data)):
        if firstname in data[i]:
            return data[i]



