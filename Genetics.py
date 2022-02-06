inpt = input()
inpt = inpt.split(' ')
n,m,k = int(inpt[0]),int(inpt[1]),int(inpt[2])
inputs = []
for _ in range(n):
    inputs.append(input())
comp = inputs[-1]
for i in inputs:
    diff = 0
    for j in range(m):
        if comp[j] != i[j]:
            diff += 1
    if diff == k:
        x = inputs.index(i)+1
print(x)
