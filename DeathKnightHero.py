rge = int(input())
count = 0
for _ in range(rge):
    battles = input()
    for i in range(len(battles)):
        if battles[i] == 'C':
            if i+1 < len(battles):
                if battles[i+1] == 'D':
                    count += 1
                    break
print(rge - count)