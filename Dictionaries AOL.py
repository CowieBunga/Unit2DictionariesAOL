
# Question 1 - Extreme Tuple

# this function determines the min and max values and returns them, or if the list is blank, it returns a statement


def extremeTuple(args):
    if len(args) > 1:  # if args has a length greater than 1, then the function will return max and min values
        maximum = max(args)
        minimum = min(args)
        return maximum, minimum
    else:  # otherwise, it returns zero, which contains the string below
        zero = "Your tuple contained no arguments or was too short"
        return zero


list1 = []   # list has to be used here because tuples are immutable
while True:  # loop allows the user to input multiple values
    nums = input("Input a number: ")
    if len(nums) > 0:  # it only appends to the list if a value was inputted (otherwise, the tuple's length will > 0)
        list1.append(nums)
    again = input("Would you like to input another value? (no to exit) ")
    if again == 'no':
        break  # breaks the loop once user is done inputting numbers.
args = tuple(list1)  # turns the list to a tuple because it needs to be returned as a tuple
results = extremeTuple(args)  # results is either max and min or zero depending on the length
print(results)  # prints the correct returned value


# Question 2 - Database


import csv
data = {}
names = ('Cowie', 'Dart', 'Otton', 'Gomes', 'Ridolfi', 'Bates')
# chose tuples for names because they can be accessed by index and I don't want them to ever change values

with open('database', 'r') as database:
    read = csv.reader(database)  # syntax that was found online
    rows = [row for row in read]  # this line makes the entire file into a list of lists

for i in range(len(rows)):
        data[names[i]] = tuple(rows[i])
print(data)

''' 
changes the list into a dictionary by going through the name tuple above and making the name in each line the 
key to the values regarding it. I chose to use a dictionary with tuples as values because it would be easy to
access the info by a key, the values don't need to change, and i wanted to access the specific information wanted 
through an index.
'''

while True:  # allows user to continue searching
    name = input("Please input the last name of the student you would like to search or 'e' to exit: ").title()
    if name in names:  # ensures that the name is valid
        '''
        the series of conditional statements below asks the user if they want to display a certain piece of info, and
        if they do, it makes a variable dedicated to that information equal to the position that it would be in in
        the dictionary. otherwise, it makes the value equal to nothing because there would be an error if the value
        is equal to nothing when it it being displayed.
        '''
        lname = input("LAST NAME? (y for yes) ")
        if lname == 'y':
            L = data[name][0]
        else:
            L = ''
        fname = input("FIRST NAME? (y for yes) ")
        if fname == 'y':
            F = data[name][1]
        else:
            F = ''
        grade = input("GRADE? (y for yes) ")
        if grade == 'y':
            G = data[name][2]
        else:
            G = ''
        house = input("HOUSE? (y for yes) ")
        if house == 'y':
            H = data[name][3]
        else:
            H = ''
        advisor = input("ADVISOR? (y for yes) ")
        if advisor == 'y':
            A = data[name][4]
        else:
            A = ''
        # code below neatly displays each piece of info whether it is blank or not.
        print("LNAME: ", L)  # the description said that the last name needs to come first
        print("FNAME: ", F)
        print("GRADE: ", G)
        print("HOUSE: ", H)
        print("ADVISOR: ", A)
    elif name == 'E':
        print("Thank you for using our database!")
        break  # exits the program
    else:
        print("That name was not in the database. Try again")



# Question 3 - One Hop

'''
the function below goes through each possible flight in the first city inputted. if the 'item' isn't the second
city (as we don't want to go right there), it will check if city 2 is in the listed flights in one of the other 
destinations of city 1. if the flight to the second city is available, the variable x is increased by one. the x value 
is necessary because there are multiple cities in each value. then, it checks if the value of x is greater than or 
equal to 1 (could possibly have two one-hop flights) and if so, it returns true.
'''

def one_hop(flights, city1, city2):
    x = 0
    for item in flights[city1]:
        if item != city2:
            if city2 in flights[item]:
                x += 1
    if x >= 1:
        return True
    else:
        return False

flights = {'Montreal': ['Toronto', 'Tampa Bay'], 'Toronto': ['Montreal', 'Tampa Bay'],
                'Tampa Bay': ['Atlanta', 'Toronto'], 'Atlanta': ['Tampa Bay']}  # the question doesn't imply that the
# example dict can't be used
city1 = input("Input first city: ").title()
city2 = input("Input second city: ").title()
print(one_hop(flights, city1, city2))  # prints either true or false


# Question 4 - Mind Reader

'''
the def below chooses the computer's guess depending on the last three inputs by the user. if there is less than three
values, the comp will guess 2. the computer will choose 1 of 8 combinations depending on the last three guesses.
'''


def choose_guess(guesses):
    if len(guesses) < 3:
        compguess = 2
    else:
        guesses = tuple(guesses)  # guesses are changes to tuples because the keys are tuples
        combinations = {(1,1,1): 1, (1,1,2): 1, (1,2,2): 2, (2,2,2): 2, (2,1,1): 1, (2,2,1): 2, (2,1,2): 2, (1,2,1): 1}
        compguess = combinations[guesses]
    return compguess


userpoints = 0
comppoints = 0
# scores for user and comp ^
guesses = []
while comppoints < 30 and userpoints < 30:  # loop runs until someone reaches 30 points.
    guess = input("Input a number between 1 and 2 ")
    if guess == '1' or guess == '2':  # had to make it so the guesses were strings for defensive coding
        guesses.append(int(guess))  # makes the guess an integer when appended to the list
        if len(guesses) > 3:  # don't want to delete values if the list is too small
            del guesses[0]  # deletes the least recent guess if the list is greater than length of 3
        if choose_guess(guesses) == int(guess):  # runs the function and checks if compguess is equal to userinput
            print("Computer got the point")
            comppoints += 1  # adds point for the comp
        else:
            print("User got the point")
            userpoints += 1  # adds point for the user
        print("User score:", userpoints)
        print("Computer Score:", comppoints)
        # prints out the score after each round

if userpoints > comppoints:  # outputs certain message depending on who got the higher score
    print("You Won! Congrats!")
else:
    print("You lost! The computer bested you.")
