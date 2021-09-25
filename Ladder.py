import math
numbers = input()
h,v = numbers.split(' ')
h = int(h)
v = int(v)
output = h/math.sin(math.radians(v))
output = (output + 0.9999999999999999999999999999999999999999999999999999999999999999999) // 1
print(int(output))