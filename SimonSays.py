rge = int(input())
lst = []
for _ in range(rge):
    command = input()
    if 'Simon says' in command:
        command = command[11:]
        lst.append(command)
for i in lst:
    print(i)