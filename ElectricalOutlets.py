rge = int(input())
for _ in range(rge):
    outlets = 0
    inpt = input()
    inpt = inpt.split(' ')
    for i in range(0, len(inpt)):
        inpt[i] = int(inpt[i])
    for i in range(1, 1+inpt[0]):
        outlets += inpt[i]-1
    print(outlets+1)