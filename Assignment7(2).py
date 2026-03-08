#Create a Menu Driven program for showing details of a Bank Account by implementing different functions for the following:a) Display the current Balanceb) Mechanism to Deposit an amountc) Mechanism to Withdraw an amount
bal = 0

def show():
    print("Current Balance:", bal)

def deposit():
    global bal
    x = int(input("Enter amount to deposit: "))
    bal = bal + x
    print("Amount Deposited")

def withdraw():
    global bal
    x = int(input("Enter amount to withdraw: "))

    if x > bal:
        print("Insufficient Balance")
    else:
        bal = bal - x
        print("Amount Withdrawn")


while True:

    print("\n--- BANK MENU ---")
    print("1 Show Balance")
    print("2 Deposit")
    print("3 Withdraw")
    print("4 Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        show()

    elif ch == 2:
        deposit()

    elif ch == 3:
        withdraw()

    elif ch == 4:
        break

    else:
        print("Wrong choice")