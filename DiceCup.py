from collections import Counter
inpt = input()
a,b = inpt.split(' ')
a,b = int(a),int(b)
valList = []

for i in range(1,a+1):
    for j in range(1,b+1):
        valList.append(i+j)

c = Counter(valList)

orderedList = c.most_common()

highest = orderedList[0][1]

for i in orderedList:
    if i[1] == highest:
        print(i[0])