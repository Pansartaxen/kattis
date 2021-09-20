cases = int(input())
citiesList = []
for _ in range(cases):
    caseList = []
    cases = int(input())
    for _ in range(cases):
        caseList.append(input())
    citiesList.append(caseList)
for i in citiesList:
    print(len(set(i)))