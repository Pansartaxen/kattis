import math
inpt = ''
while inpt != '0 0':
    inpt = input()
    D,V = inpt.split(' ')
    D,V = int(D), int(V)
    x = 2*((math.pi*((D/2)**2)*(D/2))/3)
    x = x - V 
    d = ((x*(4/(math.pi)))**(1/3))
    d = d + 2*d
    print(d)