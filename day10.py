
import re


def parse_line(line):
    # position=<-19880,  30162> velocity=< 2, -3>
    m = re.search(
        r".*\<\s*(-?\d+),\s*(-?\d+)\>.*\<\s*(-?\d+),\s*(-?\d+)\>", line)
    return {
        "position": (int(m.group(1)), int(m.group(2))),
        "velocity": (int(m.group(3)), int(m.group(4))),
    }

def empty_field(max_x, max_y):
    return [[' ' for x in range(max_x)] for y in range(max_y)]

def build_field(points):
    min_x = min(points, key=lambda p: p["position"][0])["position"][0]
    min_y = min(points, key=lambda p: p["position"][1])["position"][1]
    max_x = max(points, key=lambda p: p["position"][0])["position"][0]
    max_y = max(points, key=lambda p: p["position"][1])["position"][1]
    print ((min_x, min_y))
    print ((max_x, max_y))

    field = empty_field(max_x - min_x + 1, max_y - min_y + 1)

    for point in points:
        position = point["position"]
        x = position[0] - min_x
        y = position[1] - min_y
        field[y][x] = '#'
       
    return field


def visualize(field):
    for row in field:
        print(''.join(row))


def swap(field):
    new_field = empty_field(len(field), len(field[0]))
    for y in range(len(field)):
        for x in range(len(field[0])):
            new_field[x][y] = field[y][x]
    return new_field


def candidate(point):
    point_count = {}
    for point in points:
        x = point["position"][0]
        if x not in point_count:
            point_count[x] = 0
        point_count[x] += 1
    
    for k,v in point_count.items():
        if v > 5:
            return True

    return False

def field_size(point):
    min_x = min(points, key=lambda p: p["position"][0])["position"][0]
    min_y = min(points, key=lambda p: p["position"][1])["position"][1]
    max_x = max(points, key=lambda p: p["position"][0])["position"][0]
    max_y = max(points, key=lambda p: p["position"][1])["position"][1]

    return (max_x - min_x + 1, max_y - min_y + 1)


def step(points):
    for point in points:
        init_pos = point["position"]
        velocity = point["velocity"]
        point["position"] = (init_pos[0] + velocity[0],
                             init_pos[1] + velocity[1])
                


with open('day10.txt', 'r') as data:
    lines = data.readlines()
    points = list(map(parse_line, lines))

    last_y = None
    for i in range(100000):
        size = field_size(points)
        # if last_y is None:
        #     last_y = size[1]
        #     print(size)
        # elif last_y > size[1]:
        #     last_y = size[1]
        #     print(last_y)
        # elif last_y < size[1]: 
        if size[1] < 20 and size[1] > 0        :   
            print("------------------- " + str(i) + "--------------")
            field = build_field(points)
            visualize(field)
            # break


        step(points)        
        # print(field_size(points))
        # if candidate(points):
        #     print('----------------------------')
        #     field = build_field(points)
        #     visualize(field)
            



