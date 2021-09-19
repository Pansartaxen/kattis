"""Funkar men överstiger runtime"""
inpt = input()
inpt = inpt.split(' ')
if len(inpt) == len(set(inpt)):
    print('yes')
else:
    print('no')