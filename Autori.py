name = input()
name = name.split('-')
output = ''
for i in name:
    output = output + i[0]
print(output)