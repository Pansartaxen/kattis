inpt = input()
le = int(len(inpt)/3)
x,y,z = inpt[:le],inpt[le:le*2],inpt[le*2:]
if x == y:
    print(x)
elif x == z:
    print(x)
elif y == z:
    print(y)