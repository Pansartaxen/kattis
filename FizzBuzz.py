numbers = input()
x,y,n = numbers.split(' ')
x = int(x)
y = int(y)
n = int(n)
for i in range(1, 1+n):
    if i%x == 0 and i%y != 0:
        print('Fizz')
    elif i%x != 0 and i%y == 0:
        print('Buzz')
    elif i%x == 0 and i%y == 0:
        print('FizzBuzz')
    else:
        print(i)