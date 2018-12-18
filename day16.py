
class Sample:
    def __init__(self, before, after, call):
        self.call = call
        self.before = before
        self.after = after


def addr(state, a, b, c):
    state[c] = state[a] + state[b]
    return state


def addi(state, a, b, c):
    state[c] = state[a] + b
    return state


def mulr(state, a, b, c):
    state[c] = state[a] * state[b]
    return state


def muli(state, a, b, c):
    state[c] = state[a] * b
    return state


def banr(state, a, b, c):
    state[c] = state[a] & state[b]
    return state


def bani(state, a, b, c):
    state[c] = state[a] & b
    return state


def borr(state, a, b, c):
    state[c] = state[a] | state[b]
    return state


def bori(state, a, b, c):
    state[c] = state[a] | b
    return state


def setr(state, a, b, c):
    state[c] = state[a]
    return state


def seti(state, a, b, c):
    state[c] = a
    return state


def gtir(state, a, b, c):
    if a > state[b]:
        state[c] = 1
    else:
        state[c] = 0
    return state


def gtri(state, a, b, c):
    if state[a] > b:
        state[c] = 1
    else:
        state[c] = 0
    return state


def gtrr(state, a, b, c):
    if state[a] > state[b]:
        state[c] = 1
    else:
        state[c] = 0
    return state


def eqir(state, a, b, c):
    if a == state[b]:
        state[c] = 1
    else:
        state[c] = 0
    return state


def eqri(state, a, b, c):
    if state[a] == b:
        state[c] = 1
    else:
        state[c] = 0
    return state


def eqrr(state, a, b, c):
    if state[a] == state[b]:
        state[c] = 1
    else:
        state[c] = 0
    return state


def run_op(fn, params, state):
    old_state = list(state)
    return fn(old_state, params[1], params[2], params[3])


def valid_op(fn, params, before_state, after_state):
    return after_state == run_op(fn, params, before_state)


def valid_fns(fns, params, before_state, after_state):
    valid = []
    for fn in fns:
        if valid_op(fn, params, before_state, after_state):
            valid.append(fn)
    return valid

def count_valid(fns, params, before_state, after_state):
    valid = valid_fns(fns, params, before_state, after_state)
    return len(valid)


def parse_line(lines):
    before = list(map(lambda x: int(x), lines[0][9:-1].split(", ")))
    call = list(map(lambda x: int(x), lines[1].split(" ")))
    after = list(map(lambda x: int(x), lines[2][9:-1].split(", ")))
    return Sample(before, after, call)

def parse_op(line):
    return list(map(lambda x: int(x), line.split(" ")))

test_fn = [
    addr, addi,
    mulr, muli,
    banr, bani,
    borr, bori,
    setr, seti,
    gtir, gtri, gtrr,
    eqir, eqri, eqrr
]


with open('day16.txt', 'r') as data:
    lines = data.readlines()
    lines2 = [
        "Before: [3, 2, 1, 1]\n",
        "9 2 1 2\n",
        "After:  [3, 2, 2, 1]\n"
    ]
    lines = list(map(lambda x: x.rstrip(), lines))
    calls = []
    for i in range(0, len(lines), 4):
        calls.append(parse_line(lines[i:i+3]))
    count = 0
    for call in calls:
        if count_valid(test_fn, call.call, call.before, call.after) >= 3:
            count += 1

    print(count)

    ops = {}
    while len(test_fn) > 0:
        for call in calls:
            valid = valid_fns(test_fn, call.call, call.before, call.after)
            if len(valid) == 1:
                ops[call.call[0]] = valid[0]
                test_fn.remove(valid[0])
        print(ops)
    with open('day16-prog.txt', 'r') as prog_data:
        prog_lines = prog_data.readlines()
        prog_lines = list(map(lambda x: x.rstrip(), prog_lines))

        prog = list(map(parse_op, prog_lines))
        state = [0,0,0,0]
        for op in prog:
            state = run_op(ops[op[0]], op, state)
        print(state)


