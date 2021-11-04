rge = int(input())
avenue = []
street = []

for _ in range(rge):
    inpt = input()
    a,b = inpt.split(' ')
    a = int(a)
    b = int(b)
    avenue.append(a)
    street.append(b)

avenue.sort()
rev = avenue[::-1]
posX = 0
negX = 0
index = 0
for i, j in zip(avenue, rev):
    posX += i*index
    negX += j*index
    index += 1


street.sort()
revS = street[::-1]
posY = 0
negY = 0
index = 0
for i, j in zip(street, revS):
    posY += i*index
    negY += j*index
    index += 1

totDistance = posX-negX + posY-negY

print(totDistance)