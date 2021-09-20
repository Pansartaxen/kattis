rge = float(input())
cases = int(input())
output = 0.0000000
for _ in range(cases):
    ipt = input()
    ipt = ipt.split(' ')
    output += float(ipt[0]) * float(ipt[1])
print(output*rge)