

class Node:
    def __init__(self, meta, children):
        self.meta = meta
        self.children = children
        self.value = None


def parse(items):
    child_count = items.pop(0)
    meta_count = items.pop(0)
    children = []
    meta = []
    for i in range(child_count):
        children.append(parse(items))
    for i in range(meta_count):
        meta.append(items.pop(0))
    return Node(meta, children)


def sum_meta(node):
    return sum(node.meta) + sum(list(map(sum_meta, node.children)))


def calc_value(node):
    if node.value is not None:
        return
    if len(node.children) == 0:
        node.value = sum(node.meta)
        print("Setting leaf to " + str(node.value))
        return
    for child in node.children:
        calc_value(child)

    value = 0
    for meta in node.meta:
        print("meta " + str(meta))
        if meta != 0 and meta <= len(node.children):
            print(str(value))
            value += node.children[meta - 1].value
    print("setting value to " + str(value))
    node.value = value


with open('day08.txt', 'r') as data:
    lines = data.readline()
    # lines = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
    lines = list(map(int, lines.split(" ")))
    print(lines)
    root = parse(lines)
    print(sum_meta(root))

    calc_value(root)
    print(root.value)
