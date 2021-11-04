import math
rge = int(input())
for _ in range(rge):
    inpt = input()
    v0,vin,x1,h1,h2 = inpt.split(' ')
    v0,vin,x1,h1,h2 = float(v0),float(vin),float(x1),float(h1),float(h2)
    if v0 != 0:
        t = x1/(v0*math.cos(math.radians(vin)))
        y = v0*t*math.sin(math.radians(vin))-(1/2)*9.81*t**2
        if h1+1 < y < h2-1:
            print('Safe')
        else:
            print('Not Safe')
    else:
        print('Not Safe')