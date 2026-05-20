formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format(formatter.format(1,2,3,4), formatter.format(5,6,7,8), formatter.format(9,10,11,12), formatter.format(13,14,15,16)))

