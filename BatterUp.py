palyers = int(input())
count = 0
inpt = input()
inpt = inpt.split(' ')
lst = []
for i in range(0, len(inpt)):
    inpt[i] = int(inpt[i])
for i in inpt:
    if i == -1:
        pass
    else:
        count += 1
        lst.append(i)
print(sum(lst)/count)
