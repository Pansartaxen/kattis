width = int(input())
pices = int(input())
volume = 0
for i in range(pices):
    dim = input()
    dim = dim.split(' ')
    volume += int(dim[0])*int(dim[1])
print(int(volume/width))