import re


class Node:
    def __init__(self, name):
        self.name = name
        self.waitsOn = []
        self.finished = False
        self.in_progress = False

    def duration(self):
        return ord(self.name) - 65 + 60

    def addWait(self, node):
        self.waitsOn.append(node)

    def canFinish(self):
        return next((x for x in self.waitsOn if not x.finished), None) is None

class Worker:
    def __init__(self, num):
        self.num = num
        self.finish_time = 0
        self.current_task = None

def transform_line(line):
    m = re.search(r"Step (\w) .* step (\w) can begin\.$", line)
    return (m.group(1), m.group(2))


def part_1(lines):
    nodes = {}
    for line in lines:
        if (line[0] not in nodes):
            nodes[line[0]] = Node(line[0])
        if (line[1] not in nodes):
            nodes[line[1]] = Node(line[1])
        nodes[line[1]].addWait(nodes[line[0]])

    nodes = sorted(nodes.items(), key=lambda x: x[0])

    order = []
    while len(nodes) > 0:
        for idx, val in enumerate(nodes):
            if val[1].canFinish():
                order.append(val[1].name)
                val[1].finished = True
                del nodes[idx]
                break
    print(''.join(order))

def next_worker(workers):
    return min(workers, key=lambda w: w[0])

def find_startable(nodes): 
    for val in nodes:
        if val[1].canFinish() and not val[1].in_progress:
            return val[1]
    return None


def part_2(lines):
    nodes = {}
    for line in lines:
        if (line[0] not in nodes):
            nodes[line[0]] = Node(line[0])
        if (line[1] not in nodes):
            nodes[line[1]] = Node(line[1])
        nodes[line[1]].addWait(nodes[line[0]])

    nodes = sorted(nodes.items(), key=lambda x: x[0])

    # init the workers
    workers = []
    for i in range(5):
        workers.append(Worker(i))

    current_time = 0
    while len(list(filter(lambda n: not n[1].finished, nodes))) > 0:
        # assign out tasks 
        for worker in workers:
            # print("Worker " + str(worker.num) + " finsih time is " + str(worker.finish_time))
            if worker.finish_time <= current_time:
                if worker.current_task is not None:
                    print("marking task " + worker.current_task.name + " as complete on " + str(current_time))
                    worker.current_task.finished = True
                    worker.current_task = None
                task = find_startable(nodes)
                if task is None:
                    break
                print("assigning " + task.name + " to worker " + str(worker.num) + ' at time ' + str(current_time))
                worker.finish_time = current_time + task.duration() + 1
                worker.current_task = task
                task.in_progress = True
        
        # move to next step
        if len(list(filter(lambda w: w.current_task is not None, workers))) > 0:        
            current_time = min(filter(lambda w: w.current_task is not None, workers), key=lambda x: x.finish_time).finish_time
        # print(current_time)
        # print(list(filter(lambda n: not n[1].finished, nodes)))



with open('day07.txt', 'r') as data:
    lines = data.readlines()
    lines2 = [
        "Step C must be finished before step A can begin.",
        "Step C must be finished before step F can begin.",
        "Step A must be finished before step B can begin.",
        "Step A must be finished before step D can begin.",
        "Step B must be finished before step E can begin.",
        "Step D must be finished before step E can begin.",
        "Step F must be finished before step E can begin."
    ]
    lines = list(map(transform_line, lines))

    # part_1(lines)
    part_2(lines)
