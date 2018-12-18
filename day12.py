

def process_line(line):
    splits = line.split(" => ")
    return (splits[0], splits[1].rstrip())


def get_char(patterns, data):
    for pattern, result in patterns:
        if pattern == data:
            return result
    return data[2]


def sum_pots(offset, data):
    count = 0
    for i, c in enumerate(data):
        if c == '#':
            count += (i - offset)
    return count


with open('day12.txt', 'r') as data:
    
    lines = data.readlines()
    initial = lines.pop(0)[15:].rstrip()
    lines.pop(0)
    lines = list(map(process_line, lines))
    print(lines)

    generations = 20
    padding = 150
    initial = "."*padding + initial + "."*padding
    print(initial)

    for gen in range(generations):
        new_state = initial[0:2]
        for i in range(2, len(initial)):
            sub = initial[i-2:i+3]
            res = get_char(lines, sub)

            if not gen: print(sub + " -> " + res)
            new_state += res

        print(str(gen+1) + " " + new_state)
        initial = new_state

    print(sum_pots(padding, initial))
