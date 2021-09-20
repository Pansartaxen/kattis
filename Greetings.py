greet = input()
#greet = greet.split()
for i in greet:
    if i == 'e':
        greet = greet[:1] + 'e' + greet[1:]
print(greet)