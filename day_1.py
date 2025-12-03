lines = open("input.txt").read().strip().splitlines()

pos = 50
count = 0

for line in lines:
    dir = line[0]
    dist = int(line[1:])

    count += dist // 100
    dist %= 100
    if dir == 'R':
        next = (pos + dist) % 100
        if dist > 100 - pos:
            count += int(pos != 0)
    else:
        next = ((pos - dist) % 100 + 100) % 100
        if dist > pos:
            count += int(pos != 0)
    if next == 0:
        count += 1
    pos = next
    print(next, count)
print(count)

