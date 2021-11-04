inpt = input()
indexList = []
for i in range(len(inpt)):
    if inpt[i] == ':' or inpt[i] == ';':
        if i+1 < len(inpt):
            if inpt[i+1] == ')':
                indexList.append(i)
            elif inpt[i+1] == '-':
                if i+2 < len(inpt):
                    if inpt[i+2] == ')':
                        indexList.append(i)
for i in indexList:
    print(i)