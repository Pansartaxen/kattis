from typing import Counter


rge = int(input())
temps = input()
temps = temps.split(' ')
counter = 0
for i in temps:
    if int(i) >= 0:
        pass
    elif int(i) < 0:
        counter += 1
print(counter)