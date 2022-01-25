inpt = ''
while inpt != 0:
    inpt = int(input())
    if inpt != 0:
        orderLst = []
        numberLst = []
        for _ in range(inpt):
                orderLst.append(int(input()))
        for _ in range(inpt):
                numberLst.append(int(input()))
        lst = orderLst#.sort()
        print('---',lst)
        lst.sort()
        print('---',lst)
        #outputLst = []
        for i in lst:
            index = orderLst.index(i)
            print(i)
            #print(numberLst[index])
        #€outputLst.append(numberLst[index])
    #print(outputLst)