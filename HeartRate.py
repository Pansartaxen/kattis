rge = int(input())
for _ in range(rge):
    beats = input()
    b,p = beats.split(' ')
    b = int(b)
    p = float(p)
    bpm = b*60/p
    diff = 60/p
    minABPM = abs(bpm - diff)
    maxABPM = bpm + diff
    print(f'{minABPM:.4f} {bpm:.4f} {maxABPM:.4f}')