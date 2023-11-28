
from functools import reduce

with open('day01.txt', 'r') as data:
    lines = data.readlines()
    lines = list(map(lambda x: int(x), lines))
    print(reduce((lambda x,y: x+y), lines, 0))

    # lines = [3, 3, 4, -2, -4]
    seen = set()
    freq = 0
    i = 0
    while freq not in seen:
        seen.add(freq)
        freq = freq + lines[i]
        i = (i+1) % len(lines)
    print(freq)

