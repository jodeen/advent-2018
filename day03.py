
import re
import itertools


def transform_line(line):
    m = re.search(r"#(\d+) \@ (\d+),(\d+): (\d+)x(\d+)", line)
    return (int(m.group(1)),
            (int(m.group(2)), int(m.group(3))),
            (int(m.group(4)), int(m.group(5))))


with open('day03.txt', 'r') as data:
    lines = data.readlines()
    # lines = [
    #     '#1 @ 1,3: 4x4',
    #     # '#2 @ 1,3: 4x4',
    #     # '#3 @ 1,3: 4x4',
    #     '#2 @ 3,1: 4x4',
    #     '#3 @ 5,5: 2x2'
    # ]
    lines = list(map(transform_line, lines))

    covered = set()
    twice = set()
    totalSize = 0
    for line in lines:
        start = line[1]
        size = line[2]
        tuples = itertools.product(range(start[0], start[0] + size[0]),
                                   range(start[1], start[1] + size[1]))
        for tuple in tuples:
            if tuple in covered:
                twice.add(tuple)
            else:
                covered.add(tuple)
    print(len(twice))
    
    for line in lines:
        id = line[0]
        start = line[1]
        size = line[2]
        tuples = itertools.product(range(start[0], start[0] + size[0]),
                                   range(start[1], start[1] + size[1]))
        if len(twice.intersection(set(tuples))) == 0:
            print id