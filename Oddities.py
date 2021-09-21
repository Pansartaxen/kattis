rge = int(input())
numbers = []
for _ in range(rge):
    numbers.append(int(input()))
for i in numbers:
    if i%2 == 0:
        print(f'{i} is even')
    elif i%2 == 1:
        print(f'{i} is odd')