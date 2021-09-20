numbers = input()
a,b = numbers.split(' ')
a = a[::-1]
b = b[::-1]
if int(a) < int(b):
    print(int(b))
elif int(a) > int(b):
    print(int(a))