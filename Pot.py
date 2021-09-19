inpt = int(input())
numbers = []
for _ in range(inpt):
    numbers.append(input())

newNumber = 0

for i in numbers:
    integer = int(i[0:-1])
    power = int(i[-1])
    newNumber += integer ** power

print(newNumber)