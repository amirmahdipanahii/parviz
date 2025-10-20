space = 9
for c in range(1,10,1):
    print(space * " ","*" * c)
    space -= 1

space = 0
for c in range(10,0,-1):
    print(space * " ","*" * c)
    space += +1