rge = int(input())
inputList = []

for _ in range(rge):
    #indexList = []
    inpt = input()
    inpt = inpt.split(' ')
    for i in range(0, len(inpt)):
        inpt[i] = int(inpt[i])
    inputList.append(inpt)

for i in inputList:
    if i[0] == (i[1] - i[2]):
        print('does not matter')
    elif i[0] > (i[1] - i[2]):
        print('do not advertise')
    elif i[0] < (i[1] - i[2]):
        print('advertise')
