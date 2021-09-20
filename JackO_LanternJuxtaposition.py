numbers = input()
numbers = numbers.split(' ')
output = 1
for i in numbers:
    output = output * int(i)
print(output)