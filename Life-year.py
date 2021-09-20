cases = int(input())
periods = []
for _ in range(cases):
    qual = input()
    qual = qual.split(' ')
    periods.append(qual)
quality = 0.00
for i in periods:
    quality += float(i[0]) * float(i[1])
print(quality)