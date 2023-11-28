import re

def transform_line(line):
    m = re.search(r"(\d+), (\d+)$", line)
    return (int(m.group(1)), int(m.group(2)))

def distance(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def do_count(field, ignore):
    counts = {}
    for row_num in range(len(field)):
        for col_num in range(len(field[row_num])):
            c = field[row_num][col_num]
            if c in ignore:
                continue
            if c not in counts:
                counts[c] = 0
            counts[c] += 1
    return counts

def part_1(lines) :
    max_x = max(lines, key=lambda e: e[1])[1] +175
    max_y = max(lines, key=lambda e: e[0])[0] +175
    

    field = [['.' for x in range(max_y)] for y in range(max_x)]

    points = []
    for point in enumerate(lines):
        c = chr(65 + point[0])
        coord = point[1]
        field[coord[1]][coord[0]] = c
        points.append((c, coord))


    for row_num in range(max_x):
        for col_num in range(max_y):
            min_val = -1  
            if field[row_num][col_num] == '.':               
                for point in points:
                    dist = distance((col_num, row_num), point[1])
                    if min_val < 0 or dist < min_val:
                        min_val = dist
                        field[row_num][col_num] = point[0]
                    elif dist == min_val:
                        field[row_num][col_num] = '.'

    infinite = set(list(field[0]))
    infinite = infinite.union(list(field[len(field)-1]))
    for row in field:
        infinite.add(row[0])
        infinite.add(row[len(row)-1])
    print(infinite)

    counts = do_count(field, infinite)
    print(counts)


def part_2(lines) :
    max_x = max(lines, key=lambda e: e[1])[1] +5
    max_y = max(lines, key=lambda e: e[0])[0] +5
    

    field = [['.' for x in range(max_y)] for y in range(max_x)]

    points = []
    for point in enumerate(lines):
        c = chr(65 + point[0])
        coord = point[1]
        field[coord[1]][coord[0]] = c
        points.append((c, coord))


    for row_num in range(max_x):
        for col_num in range(max_y):
            dist_sum = 0              
            for point in points:
                dist = distance((col_num, row_num), point[1])
                dist_sum += dist
            if dist_sum < 10000:
                field[row_num][col_num] = '#'

    counts = do_count(field, set('.'))
    print(counts)



with open('day06.txt', 'r') as data:
    lines = data.readlines()
    lines2 = ["1, 1",
     "1, 6",
     "8, 3",
     "3, 4",
     "5, 5",
     "8, 9"]
    lines = list(map(transform_line, lines))


    # part_1(lines)
    part_2(lines)


    # print(field[11][0])
    # for row in field:
    #     print(''.join(row))
