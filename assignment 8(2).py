#Copy a Python file but remove comments, and show content of both files.
src = input("Enter source python file name: ")
dest = input("Enter destination file name: ")

f1 = open(src, "r")
lines = f1.readlines()
f1.close()

f2 = open(dest, "w")

for line in lines:
    # skip comment lines
    if line.strip().startswith("#"):
        continue
    else:
        f2.write(line)

f2.close()

print("\nSource file content:\n")

f1 = open(src, "r")
print(f1.read())
f1.close()

print("\nDestination file content (without comments):\n")

f2 = open(dest, "r")
print(f2.read())
f2.close()