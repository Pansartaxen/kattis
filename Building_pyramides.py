inpt = int(input())
side_length = 1
layer = 0
blocks = 0
while (blocks + side_length * side_length) <= inpt:
    blocks += side_length*side_length
    side_length += 2
    layer += 1

print(layer)