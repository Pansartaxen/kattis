numbers = input()
a,b = numbers.split(' ')
a = int(a)
b = int(b)
if a>b:
    print(f'{a} {b}')
elif a<b:
    print(f'{b} {a}')