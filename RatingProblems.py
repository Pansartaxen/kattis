inpt = input()
n,k = inpt.split(' ')
n = int(n)
k = int(k)
ratings = []

for _ in range(k):
    score = int(input())
    ratings.append(score)

if k == n:
    scores = sum(ratings)/k
    print(f'{scores}  {scores}')
else:
    minScore = (sum(ratings)-(3*(n-k)))/n
    maxScore = (sum(ratings)+(3*(n-k)))/n
    print(f'{minScore}  {maxScore}')