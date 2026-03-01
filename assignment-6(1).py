#Develop an application which asks the user to enter a string and prints its statistics as:
#a) Number of Vowels
#b) Number of Consonants
#c) Number of Spaces
#d) Number of Lowercase Letters
x = input("Enter a string: ")

v = 0
c = 0
s = 0
l = 0

for ch in x:
    if ch in "aeiouAEIOU":
        v += 1
    elif ch == " ":
        s += 1
    elif ch.isalpha():
        c += 1

    if ch.islower():
        l += 1

print("Vowels:", v)
print("Consonants:", c)
print("Spaces:", s)
print("Lowercase letters:", l)