from sys import argv

script, first, second, third = argv

print(type(argv))
print(len(argv))

print("the script is called:", script)
print("the first var is:", first)
print("the second var is:", second)
print("the third var is:", third)


print("&&&&&&&&&&&")

for i in argv:
    print(i)
