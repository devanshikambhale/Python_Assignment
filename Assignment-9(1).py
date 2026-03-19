# Create a class Employee and inherit it into another class Manager. Add methods to take input and display employee details. Consider attributes like name, age, salary, address. Process the information of 10 managers.
# program for employee and manager using inheritance

class Employee: 
    def __init__(self):
        self.name = ""      # employee name
        self.age = 0        # employee age
        self.salary = 0     # salary
        self.address = ""   # address

    def take_input(self):
        # taking input
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = float(input("Enter salary: "))
        self.address = input("Enter address: ")

    def display(self):
        # display data
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


class Manager(Employee):
    def __init__(self):
        super().__init__()   # call parent constructor
        self.dept = ""       # department

    def take_input(self):
        super().take_input()   # take employee data
        self.dept = input("Enter dept: ")

    def display(self):
        super().display()   # show employee data
        print("Dept:", self.dept)


def main():
    managers = []   # list for managers

    for i in range(10):
        print("\nManager", i+1)
        m = Manager()
        m.take_input()
        managers.append(m)   # add to list

    print("\nDetails:")
    for m in managers:
        m.display()   # show data


main()   # call main