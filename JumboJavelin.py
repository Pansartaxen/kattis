rge = int(input())
inputList = []
for _ in range(rge):
    inputList.append(int(input()))
totLength = sum(inputList)

print(totLength-(rge-1))