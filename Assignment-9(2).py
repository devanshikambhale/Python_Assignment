# Create a Library Management System with:
# Classes for Book, Member, and Library
# Methods to add books, issue books, return books, and display books
# A menu-driven program
# simple library program

class Book:
    def __init__(self):
        self.id = 0        # book id
        self.name = ""     # book name
        self.issued = False   # check issued or not


class Library:
    def __init__(self):
        self.list = []    # list to store books

    def add(self):
        b = Book()
        b.id = int(input("id: "))
        b.name = input("name: ")
        self.list.append(b)   # add book in list

    def show(self):
        # display all books
        for b in self.list:
            print(b.id, b.name, b.issued)

    def issue(self):
        x = int(input("enter id: "))
        for b in self.list:
            if b.id == x:
                if b.issued == False:
                    b.issued = True
                    print("issued")
                    return
        print("not found")

    def ret(self):
        x = int(input("enter id: "))
        for b in self.list:
            if b.id == x:
                if b.issued == True:
                    b.issued = False
                    print("returned")
                    return
        print("error")


l = Library()   # object

while True:
    # menu
    print("1 add 2 show 3 issue 4 return 5 exit")
    ch = int(input())

    if ch == 1:
        l.add()

    elif ch == 2:
        l.show()

    elif ch == 3:
        l.issue()

    elif ch == 4:
        l.ret()

    elif ch == 5:
        break