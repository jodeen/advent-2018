from typing import Dict, Tuple, List

def ccw(idx, num, items):
    return (idx - num) % len(items)
def cw(idx, num, items):
    return (idx + num) % len(items)

def add_new(current: int, new_num: int, items: List[int], current_player:int, players: Dict[int, int]) -> int:
    if new_num % 23 == 0:
        # print("----")
        idx = ccw(current, 7, items)
        players[current_player] += new_num + items.pop(idx)
        # return cw(idx, , items)
        return idx
    else:
        idx = cw(current, 1, items) + 1
        items.insert(idx, new_num)
        return idx

def output(current, items):
    for idx, item in enumerate(items):
        if (idx == current):
            print(' (' + str(item) + ') ', end='')
        else:
            print(' ' + str(item) + '  ', end='')
    print('')

def part1():
    player_count = 416
    marbles = 7161700

    current = 0
    items = []
    items.append(0)
    scores = {}
    current_player = 0
    
    for i in range(1, marbles + 1):
        current_player = i % player_count
        if current_player not in scores:
            scores[current_player] = 0
        
        current = add_new(current, i, items, current_player, scores)
        # print(str(current) + " - " + str(items))
        # output(current, items)
    print(scores)
    print(max(scores.values()))
    


part1()