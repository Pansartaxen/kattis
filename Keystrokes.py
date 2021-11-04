password = input()
commandList = []
for i in range(len(password)):
    if password[i] == 'L':
        commandList.append('L')
    elif password[i] == 'R':
        commandList.append('R')
    elif password[i] == 'B':
        commandList.append('B')

password = password.replace('L', '')
password = password.replace('R', '')
password = password.replace('B', '')

if len(commandList) == 0:
    print(password)
else:
    print(commandList)