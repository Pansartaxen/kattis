rge = int(input())
numbers = []
for _ in range(rge):
    numbers.append(int(input()))
for i in numbers:
    if i//2 == i/2:
        print(f'{i} is even')
    elif i//2 != i/2:
        print(f'{i} is odd')