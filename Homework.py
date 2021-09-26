inpt = input()
inpt = inpt.split(';')
lst = []
for i in inpt:
    if '-' in i:
        a,b = i.split('-')
        for x in range(int(a), int(b)+1):
            lst.append(x)
    else:
        lst.append(i)
#print(lst)
print(len(lst))