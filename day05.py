import string

def react(a, b):
    if a == b: return False
    if a.upper() == b:
        return True
    if a.lower() == b:
        return True
    return False

def simplify(line):
    has_reaction = True
    while has_reaction:
        has_reaction = False
        idx = 0

        while idx < len(line)-1:
            a = line[idx]
            b = line[idx + 1]
            
            if react(a,b):
                del line[idx]
                del line[idx]
                idx -= 1
                if idx < 0: idx = 0
                has_reaction = True
            else:
                idx += 1
    return ''.join(line)

def remove_char(line, c):
    return list(filter(lambda x: x.lower() != c.lower(), line))



with open('day05.txt', 'r') as data:
    line = data.readline().strip("\n")
    # line = "dabAcCaCBAcCcaDA"
    line = list(line)

    s_line = simplify(line)
    print(len(s_line))


with open('day05.txt', 'r') as data:
    chars = []
    for char in string.ascii_lowercase:
        chars.append(char)

    line = data.readline().strip("\n")
    # line = "dabAcCaCBAcCcaDA"
    line = list(line)

    min_char = 'a'
    min_count = -1
    # chars = list("abcd")
    for char in chars:
        reduced_line = remove_char(list(line), char)
        s_line = simplify(reduced_line)
        # print(reduced_line)
        # print(s_line)
        # print()
        if min_count < 0 or len(s_line) < min_count:
            min_count = len(s_line)
            min_char = char
    
    print(min_count)
    print(min_char)

    # print(''.join(line))
    # print(len(line))
