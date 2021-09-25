numbers = input()
wc,hc,ws,hs = numbers.split(' ')
wc = int(wc)
hc = int(hc)
ws = int(ws)
hs = int(hs)
if wc >= ws+2 and hc >= hs+2:
    print(1)
else:
    print(0)