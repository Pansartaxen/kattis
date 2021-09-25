numbers = input()
order = input()
outputList = []
numbers = numbers.split(' ')
for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])
numbers.sort()
a = numbers[0]
b = numbers[1]
c = numbers[2]
for i in order:
    if i == 'A':
        outputList.append(a)
    elif i == 'B':
        outputList.append(b)
    elif i == 'C':
        outputList.append(c)
print(f'{outputList[0]} {outputList[1]} {outputList[2]}')