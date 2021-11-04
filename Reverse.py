rge = int(input())
numbers = []
for _ in range(rge):
    x = int(input())
    numbers.append(x)
numbers.reverse()
for i in numbers:
    print(i)