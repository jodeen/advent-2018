
def empty_field(max_x, max_y):
    return [[0 for x in range(max_x)] for y in range(max_y)]


def part2(levels):
    max_x = 300
    max_y = 300
    max_val = 3
    field = [[[] for x in range(max_x)] for y in range(max_y)]
    for row_num, row in enumerate(field):
        for col_num, col in enumerate(row):
            values = field[row_num][col_num]
            values.append(levels[row_num][col_num])
            for i in range(1, min(max_x - col_num, max_y - row_num, max_val)):
                last = values[-1]
                for j in range(i):
                    last += levels[row_num][col_num + j]
                    last += levels[row_num + j][col_num]
                    
    m = None
    m_v = None
    for row_num, row in enumerate(field):
        for col_num, col in enumerate(row):
            if m is None or m_v < field[row_num][col_num][2]:
                m_v = field[row_num][col_num][2]
                m = (col_num, row_num)
    print((m, m_v))
                







def fill_grid(field):
    for row_num, row in enumerate(field):
        for col_num, col in enumerate(row):
            field[row_num][col_num] = calc_power(col_num + 1, row_num + 1)


def calc_grid(levels, size):
    print('calcing grid :' + str(size))
    values = empty_field(len(levels[0]), len(levels))
    for row_num in range(len(levels)):
        for col_num in range(len(levels)):
            values[row_num][col_num] = sub(levels, size, col_num, row_num)
    return values


def find_max(grid):
    max_coord = None
    max_val = None
    for row_num in range(len(grid)):
        for col_num in range(len(grid)):
            val = grid[row_num][col_num]
            if max_val is None or val > max_val:
                max_val = val
                max_coord = (col_num, row_num)
    return (max_coord, max_val)


def sub(field, size, col, row):
    acc = 0
    for row in field[row:row+size]:
        for cell in row[col:col+size]:
            acc += cell
    return acc


def factor(num):
    if num in primes:
        return (num, 1)
    for prime in primes:
        if num % prime == 0:
            return (int(num/prime), prime)
    return None


# def find_max(field, size):
#     max_coord = None
#     max_val = None
#     for row_num, row in enumerate(field):
#         for col_num, cell in enumerate(row):
#             val = sub(field, size, col_num, row_num)
#             if max_val is None or val > max_val:
#                 max_coord = (col_num, row_num)
#                 max_val = val

#     return (max_coord, max_val, size)


def calc_power(col, row):
    rack_id = col + 10
    power_level = rack_id * row
    power_level += serial_num
    power_level *= rack_id
    hund = int((power_level % 1000) / 100)
    return hund - 5


def visualize(field):
    for row in field:
        print('  '.join(map(lambda x: str(x), row)))


serial_num = 18
primes = [
    1 , 2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
    127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
    179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
    233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
    283, 293
    ]
primes.reverse()
print(primes)

levels = empty_field(300, 300)
fill_grid(levels)

levels2 = [[-2, -4, 4, 4, 4],
           [-4,  4,  4,  4, -5],
           [4, 3,  3,  4, -4],
           [1, 1,  2,  4, -3],
           [-1, 0,  2, -5, -2]]
# visualize(field)

# print(find_max(field, 3))

# print(factor(300))

grid2 = calc_grid(levels, 16)
print(find_max(grid2))

memo = {
    1: levels
}

part2(levels)

# for i in range(300):
#     factors = factor(i+1)
#     # print(i+1)
#     print(factors)
#     grid = calc_grid(memo[factors[1]], factors[0])
#     memo[i+1] = grid
#     print(memo.keys())


# m = None
# for size in range(301):
#     print(size)
#     n = find_max(field, size)
#     if m is None or n[1] > m[1]:
#         m = n
