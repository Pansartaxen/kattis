# for _ in range(3):
#     numbers = input()
#     xy = numbers.split(' ')
#     x = int(xy[0])
#     y = int(xy[1])
#     print(abs(x-y))

import sys

for i in sys.stdin:
  ab = i.split()
  a = int(ab[0])
  b = int(ab[1])
  print(abs(a - b))