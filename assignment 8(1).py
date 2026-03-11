#Read a text file and write the same content in UPPERCASE to another file#
src = input("Enter source file name: ")
dest = input("Enter destination file name: ")

# open source file
f1 = open(src, "r")

text = f1.read()   # read file content
f1.close()

text = text.upper()   # convert text into uppercase

# open destination file
f2 = open(dest, "w")

f2.write(text)   # write data into new file
f2.close()

print("File copied successfully")
print("\nContent written in destination file:\n")
print(text)