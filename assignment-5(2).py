#Create a program to store the prices of sold items on a particular day in a Tuple. Perform the following operations:
#a) Print total number of items sold
#b) Print price of cheapest item sold
#c) Print price of costliest item sold
#d) Print price list in ascending order
#e) Print number of costliest items sold
x = input("Enter prices separated by space: ")

y = tuple(map(int, x.split()))

print("Prices:", y)

print("Total items sold:", len(y))

print("Cheapest item price:", min(y))

print("Costliest item price:", max(y))

z = sorted(y)
print("Prices in ascending order:", z)

c = y.count(max(y))
print("Number of costliest items sold:", c)