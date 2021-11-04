spam = input()
underCount = 0
lowCount = 0
uppCount = 0
symbCount = 0
for i in spam:
    if i == '_':
        underCount += 1
    elif i == i.lower() and i.isalpha():
        lowCount += 1
    elif i == i.upper() and i.isalpha():
        uppCount += 1
    else:
        symbCount += 1
print(underCount/len(spam))
print(lowCount/len(spam))
print(uppCount/len(spam))
print(symbCount/len(spam))