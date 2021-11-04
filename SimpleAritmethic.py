from decimal import Decimal
numbers = input()
numbers = numbers.split(' ')
for i in range(len(numbers)):
    numbers[i] = float(numbers[i])
output = Decimal(numbers[0]) * (Decimal(numbers[1])/Decimal(numbers[2]))
print(output)