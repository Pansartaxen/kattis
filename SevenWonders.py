inpt = input()
t = 0
g = 0
c = 0
for i in inpt:
    if i == 'T':
        t += 1
    elif i == 'G':
        g += 1
    elif i == 'C':
        c += 1
bonus = min(t,g,c)*7
output = t**2 + g**2 + c**2 + bonus
print(output)