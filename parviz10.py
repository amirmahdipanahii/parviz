space = 9
for c in range(1,21,2):
    print(space * " ","*" * c)
    space -= 1
space = 1
for c in range(17,0,-2):
    print(space * " ","*" * c)
    space += 1