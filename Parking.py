cases = int(input())
for _ in range(cases):
    dist = 0
    stores = int(input())
    numbers = input()
    numbers = numbers.split(' ')
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    numbers.sort()
    for i in range(len(numbers)):
        if i+1 < len(numbers):
            dist += numbers[i+1] - numbers [i]
        else:
            dist += numbers[i] - numbers[0]
    print(dist)