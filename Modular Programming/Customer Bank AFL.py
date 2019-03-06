class Customer:
    def __init__(self, username, password, balance):
        self.deposits = [0]  # lists to keep track of transactions
        self.withdrawals = [0]
        self.username = username
        self.password = password
        self.balance = balance

    def makeDeposit(self, dValue):
        self.deposits.append(dValue)
        self.balance = str(int(self.balance)+ dValue)

    def makeWithdrawal(self, wValue):
        self.withdrawals.append(wValue)
        self.balance = str(int(self.balance)- wValue)

    def printBalance(self):
         return user.balance

x = 0
username = input("Please input a username ")
password = input("Now input a password ")
with open('usernames', 'r') as usernames:
    u = usernames.read().splitlines()
with open('passwords', 'r') as passwords:
    p = passwords.read().splitlines()

with open('balances', 'r') as balances:
    b = balances.read().splitlines()

for i in range(0, len(u)): #error; doesn't work with other usernmaes and pwords
    if p[i] == password and u[i] == username:
        print("You are an old user!")
        balance = b[i]
        print("Your current balance is", balance)
        x = 1
        break

if x != 1:
    i = len(b)
    b.append("")
    balance = 1000
    with open('usernames', 'a') as usernames:
        usernames.write("\n" + username)
    with open('passwords', 'a') as passwords:
        passwords.write("\n" + password)


user = Customer(username, password, balance)
while True:
    choice = input("Press 'e' to exit, 'd' for deposit, 'w' for withdrawal, and 'p' for print balance ")
    if choice == 'd':
        dValue = int(input("Input how much you would like to deposit "))
        user.makeDeposit(dValue)
        b[i] = user.printBalance()
    elif choice == 'w':
        wValue = int(input("Input how much you would like to withdrawal "))
        user.makeWithdrawal(wValue)
        b[i] = user.printBalance()
    elif choice == 'p':
        print(user.printBalance())
    elif choice == 'e':
        with open('balances', 'w') as balances:
            holder = ""
            for j in b:
                holder += j+"\n"
            balances.write(holder)
        balances.close()
        break
    else:
        print("invalid input")



