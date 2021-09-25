import math
dim = input()
dim = dim.split(' ')
for i in range(0, len(dim)):
        dim[i] = int(dim[i])
x = dim[0]
b = dim[1]
h = dim[2]
messure = math.sqrt(b**2 + h**2)
for _ in range(x):
    match = int(input())
    if match <= messure:
        print('DA')
    else:
        print('NE')