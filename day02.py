
def letterCount(word):
    count = {}
    for char in word:
        if (char not in count):
            count[char] = 1
        else:
            count[char] = count[char] + 1
    return count
def hasExactCount(freq, count):
    res = {k: v for k, v in freq.items() if v == count}
    return bool(res)

def numDiff(a, b):
    counter = 0
    for x in range(0, len(a)):
        if a[x] != b[x]:
            counter += 1
    return counter

with open('day02.txt', 'r') as data:
    lines = data.readlines()

    # lines=["abcdef", "bababc", "abbcde", "abcccd","aabcdd", "abcdee", "ababab"]

    lineCount = list(map(letterCount, lines))

    twoCount = len(list(filter(lambda x: hasExactCount(x, 2), lineCount)))
    threeCount = len(list(filter(lambda x: hasExactCount(x, 3), lineCount)))

    print (twoCount * threeCount)


    for x in range(0, len(lines)):
        for y in range(x+1, len(lines)):
            a = lines[x]
            b = lines[y]

            if (len(a) == len(b) and numDiff(a,b) == 1):
                print(a)
                print(b)
                break


