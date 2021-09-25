photos = int(input())
numbersList = []
for _ in range(photos):
    inpt = input()
    inpt = inpt.split(' ')
    for i in range(0, len(inpt)):
        inpt[i] = int(inpt[i])
    numbersList.append(inpt)
speed = 0
for i in range(len(numbersList)):
    if numbersList[i][0] == 0:
        pass
    else:
        if speed < (numbersList[i][1]-numbersList[i-1][1])/(numbersList[i][0]-numbersList[i-1][0]):
            speed = (numbersList[i][1]-numbersList[i-1][1])/(numbersList[i][0]-numbersList[i-1][0])
        elif speed < numbersList[i][1]/numbersList[i][0]:
            speed = numbersList[i][1]/numbersList[i][0]
print(int(speed))