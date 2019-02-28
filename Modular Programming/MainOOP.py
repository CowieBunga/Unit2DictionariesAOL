import functions

# Class Example
'''
print(functions.returnOdd([00,11,22,33,44,55]))
'''

database = open('database2', 'r')
data = functions.csvTo2DList(database)
print(data)

firstname = functions.specialInput(data)
print(firstname)

print(functions.listQuery(data, firstname))

