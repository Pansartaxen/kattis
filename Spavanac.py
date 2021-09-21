time = input()
h,m = time.split(' ')
h = int(h)
m = int(m)
if m-45 >= 0:
    print(f'{str(h)} {str(m-45)}')
elif m-45 < 0 and h > 0:
    m = abs(m-45)
    print(f'{str(h-1)} {str(60-m)}')
elif m-45 < 0 and h <= 0:
    m = abs(m-45)
    print(f'23 {str(60-m)}')