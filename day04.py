import re


def transform_line(line):
    m = re.search(r"\[((\d+-\d+-\d+) (\d+):(\d+))] (.*)$", line)

    return {
        "full": m.group(1),
        "day": m.group(2),
        "minute": int(m.group(4)),
        "message": m.group(5)
    }


def is_guard_change(message):
    m = re.search(r"Guard #(\d+) begins shift", message)
    if (m):
        return m.group(1)
    else:
        return None


def split_by_guard(lines):
    guard = -1
    guard_entries = {}
    for line in lines:
        new_guard = is_guard_change(line['message'])
        if new_guard:
            guard = new_guard
            if guard not in guard_entries:
                guard_entries[guard] = {
                    'entries': []
                }
            guard_lines = guard_entries[guard]['entries']
        else:
            guard_lines.append(line)
    return guard_entries


def determine_sleep(guard_entry):
    sleeps = []
    start = -1
    for entry in guard_entry['entries']:
        if (entry['message'].startswith('falls')):
            start = entry['minute']
        if (entry['message'].startswith('wakes')):
            sleeps.append(range(start, entry['minute']))
            start = -1
    guard_entry['sleeps'] = sleeps    


def minutes_asleep(guard_entry):
    sum = 0
    for sleep in guard_entry['sleeps']:
        sum += (sleep.stop - sleep.start)
    guard_entry['sleep_sum'] = sum

def sleep_count(guard_entry):
    count = [0] * 60
    for sleep in guard_entry['sleeps']:
        for x in sleep:
            count[x] += 1
    guard_entry['sleep_count'] = count

def find_max_minute(guard_entry):
    max_idx = 0
    max_count = 0
    for idx, count in enumerate(guard_entry['sleep_count']):
        if count > max_count:
            max_idx = idx
            max_count = count
    return (max_idx, max_count)
  

with open('day04.txt', 'r') as data:
    lines = data.readlines()

    lines2 = [
        '[1518-11-01 00:00] Guard #10 begins shift',
        '[1518-11-01 00:05] falls asleep',
        '[1518-11-01 00:25] wakes up',
        '[1518-11-01 00:30] falls asleep',
        '[1518-11-01 00:55] wakes up',
        '[1518-11-01 23:58] Guard #99 begins shift',
        '[1518-11-02 00:40] falls asleep',
        '[1518-11-02 00:50] wakes up',
        '[1518-11-03 00:05] Guard #10 begins shift',
        '[1518-11-03 00:24] falls asleep',
        '[1518-11-03 00:29] wakes up',
        '[1518-11-04 00:02] Guard #99 begins shift',
        '[1518-11-04 00:36] falls asleep',
        '[1518-11-04 00:46] wakes up',
        '[1518-11-05 00:03] Guard #99 begins shift',
        '[1518-11-05 00:45] falls asleep',
        '[1518-11-05 00:55] wakes up'
    ]

    lines = list(map(transform_line, lines))

    lines.sort(key=lambda e: e['full'])

    guard_entries = split_by_guard(lines)

   
    for guard, entry in guard_entries.items():
        determine_sleep(entry)
        minutes_asleep(entry)
        sleep_count(entry)
    
    max_entry = max(guard_entries.items(), key=lambda e: e[1]['sleep_sum'])

    print(max_entry[1])
    print(max_entry[0])
    print(find_max_minute(max_entry[1])[0])

    maxes = []
    for guard, entry in guard_entries.items():
        maxes.append((guard, find_max_minute(entry)))        

    max_overall = max(maxes, key=lambda e: e[1][1])
    print(max_overall)

    


    # print(guard_entries)
   
