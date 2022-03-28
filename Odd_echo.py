rge = int(input())
lst = []
for i in range(rge):
    word = input()
    if i%2 == 0:
        lst.append(word)

for i in lst:
    print(i)