from sys import argv

script, filename = argv

print(f"we're going to erase {filename}.")
print("if you dont want that hit CRTL-C (^C)^C")
print("if you do want that hit return")

input("?")

print("opening the file...")
target = open(filename, 'w')

print("truncating the file, goodbye!")
target.truncate()

print("now im going to ask you for 3 lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")


print("im going to write these to file")

target.write(f"{line1}\n")
target.write(f"{line2}\n")
target.write(f"{line3}\n")

print("now closing file.")

target.close()

