'''
1 - Use a series of length 2 tuples to insert points in a 2d list (which would be a representation of the graph) and print it as a graph.
2 - Create a dictionary of strings and tuples that hold speeds for streets in both km/h and mph and then allow it to be searchable via user input.
3 - Make a function that takes in a dictionary and returns a list of tuples containing each key value pair.
'''

'''
grid = []

for i in range(0, 5):
    grid.append([])
    for j in range(0, 5):
        grid[i].append("")

while True:
    x = int(input("X Coordinate: "))
    y = int(input("Y Coordinate: "))
    y = 5-int(y)
    if x < 6 and y < 6:
        grid[y][x] = "."
        again = str(input("Would you like to input another coordinate? "))
        if again == "no":
            break

for i in range(0, 5):
    line = ""
    for j in range(0, 5):
        line = line + grid[i][j] + " "
    print(line)
'''

'''
dict = {"alabama": ("50", '31.07'), "canada": ("60", '37.28'), "california": ("70", '43.50')}
while True:
    userinput = input("please select 'alabama', 'canada' or 'california' ")
    userinput2 = input("would you like mph or km/h? ")
    if userinput2 == "km/h":
        type = 0
    elif userinput2 == 'mph':
        type = 1
    else:
        print("try again")
    print(dict[userinput][type])
'''

'''
def tuple_dict(dict):
    list1 = []
    for item in dict.keys():
        if isinstance(dict[item], tuple): # access the dictionary at that specific key, and checks if it is a tuple
            list1.append((item, dict[item]))
    return list1
dict = {"key1": (1, 15), "key2": "hello", "key3": ("my", "apple")}
list1 = print(tuple_dict(dict))
'''