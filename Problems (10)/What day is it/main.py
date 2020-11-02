offset = int(input())
if offset + 10.5 >= 24:
    print('Wednesday')
elif offset + 10.5 < 0:
    print('Monday')
else:
    print('Tuesday')
