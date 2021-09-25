distance = float(input())
realDistance = (distance*1000)*(5280/4854)
realDistance = (realDistance + 0.5) // 1
print(int(realDistance))