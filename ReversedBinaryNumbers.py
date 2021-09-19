#print(bin(11))
number = int(input())
binaryNr = bin(number)
binaryNr = binaryNr[2:]
outputNr = 0
binaryNr.split
for i in range(0,len(binaryNr)):
    if binaryNr[i] == '1':
        outputNr += 2**i
print(outputNr)