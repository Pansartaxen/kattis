import math
rge = int(input())
for _ in range(rge):
    word = input()
    leng = int(math.sqrt(len(word)))
    for j in range(1, leng+1):
        for i in range(1, leng+1):
            realWord = realWord + word[(i*leng)-j]
    print(realWord)