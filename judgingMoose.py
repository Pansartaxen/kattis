#a,b = map(int,input(.split()))
inpt = input()
a,b = inpt.split(' ')
if int(a) == 0 and int(b) == 0:
    print('Not a moose')
elif int(a) == int(b):
    print(f'Even {int(a)*2}')
elif int(a) != int(b):
    if int(a) > int(b):
        print(f'Odd {int(a)*2}')
    elif int(a) < int(b):
        print(f'Odd {int(b)*2}')