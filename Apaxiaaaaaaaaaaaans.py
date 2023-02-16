name = input()
output = ''
for i in range(len(name)):
    if i == 0:
        output = output + name[0]
    elif name[i] != name[i-1]:
        output = output + name[i]
    elif name[i] == name[i-1]:
        pass
print(output)
