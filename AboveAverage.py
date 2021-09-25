rge = int(input())
output = []
for i in range(rge):
    numbers = input()
    numbers = numbers.split(' ')
    counter = 0
    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])
    for i in range(1, len(numbers)):
        if int(numbers[i]) > (sum(numbers)-numbers[0])/numbers[0]:
            counter += 1
    perc = counter / int(numbers[0])
    perc = perc * 100
    # if perc == 75.0 or perc == 25.0 or perc == 50.0:
    #     perc = str(perc) + '00'
    # if len(str(perc)) == 5:
    #     perc = str(perc) + '0'
    # elif len(str(perc)) == 4 and perc >= 10:
    #     perc = str(perc) + '00'
    # elif len(str(perc)) == 3:
    #     perc = str(perc) + '00'
    # elif len(str(perc)) == 4 and perc < 10:
    #     perc = str(perc) + '0'
    # if type(perc) == type(1.1):
    #     perc = round(perc, 3)
    #print(f'{perc}%')
    #output.append(str(perc)+'%')
    output.append(format(perc, ".3f") + '%')
for i in output:
    print(i)