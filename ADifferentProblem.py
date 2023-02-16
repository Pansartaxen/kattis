import sys
for i in sys.stdin:
    #list = [int(i) for i in input().split('')]
    ab = i.split()
    a = int(ab[0])
    b = int(ab[1])
    print(abs(a - b))
