numberList = []
for _ in range(10):
    number = int(input())
    numberList.append(number)
outputList = []
for i in numberList:
    x = i%42
    outputList.append(x)
print(len(set(outputList)))