plan = int(input())
months = int(input())
dataLeft = 0
for _ in range(months):
    used = int(input())
    dataLeft += plan - used
print(dataLeft+plan)