trips = 0
while trips != -1:
    trips = int(input())
    if trips != -1:
        time = 0
        distance = 0
        for _ in range(trips):
            data = input()
            s,t = data.split(' ')
            s = int(s)
            t = int(t)
            t = t - time
            time += t
            distance += s*t
        print(f'{distance} miles')
    else:
        pass