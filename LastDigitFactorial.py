rge = int(input())
inputList = []
for _ in range(rge):
    number = int(input())
    inputList.append(number)

factorialList = []

for i in inputList:
    fact = 1
    for x in range(1,1+i):
        fact = fact * x
    factorialList.append(fact)

for i in factorialList:
    nr = str(i)
    output = nr[-1]
    print(int(output))