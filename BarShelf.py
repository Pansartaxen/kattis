import timeit
start = timeit.timeit()
length = int(input())
inpt = input()
inpt = inpt.split(' ')
for i in range(length):
    inpt[i] = int(inpt[i])

counter = 0
checkList = []

for i in range(length):
    x = inpt[i]
    for j in range(i+1, length):
        y = inpt[j]
        if 2*inpt[j] <= x:
            for k in range(j+1, length):
                if 2*inpt[k] <= y:
                    counter += 1

# for i in range(length-2):
#     x = inpt[i]
#     #s = sum(inpt[i+1:])
#     #if x < s:
#     lista = inpt[i+1:]
#     lista.sort
#     for j in range(len(lista)):
#         y = lista[j]
#         if 2*lista[j] <= x:
#             for k in range(j+1, len(lista)):
#                 if 2*lista[k] <= y:
#                     counter += 1

print(counter)
end = timeit.timeit()
print(end-start)
#0.00021119499999999736