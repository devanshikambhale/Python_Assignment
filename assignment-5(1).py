#Develop a program that asks the user to enter a series of integers and store them in a Tuple. Perform the following operations:
#a) Print the total number of items in the Tuple.
#b) Print the last item in the Tuple.
#c) Print the Tuple elements in reverse order.
#d) Print Yes if the Tuple contains integer 5 and No otherwise.
#e) Remove the first and last items from the Tuple, sort the remaining items, and print the result.
x = input("Enter numbers separated by space: ")

y = tuple(map(int, x.split()))

print("Tuple:", y)

print("Total elements:", len(y))

print("Last element:", y[-1])

print("Reverse tuple:", y[::-1])

if 5 in y:
    print("Yes")
else:
    print("No")

z = y[1:-1]

z = tuple(sorted(z))

print("After removing first and last and sorting:", z)