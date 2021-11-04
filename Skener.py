inpt = input()
r,c,xR,xC = inpt.split(' ')
r,c,xR,xC = int(r),int(c),int(xR),int(xC)
for _ in range(r):
    word = input()
    output = ''
    for i in word:
        output = output + i*xC
    for i in range(xR):
        print(output)