lines = open('input.txt', 'r').read().splitlines()

segs = []

def first():
    freshCount = 0
    emptySeen = False

    q = []
    for line in lines:
        if line == '':
            emptySeen = True
            continue

        if not emptySeen:
            l, r = map(int, line.split('-'))
            segs.append([l, r]) 
        else:
            q.append(int(line))           

    q.sort()
    segs.sort()
    
    ranges = []
    for l, r in segs:
        if len(ranges) == 0 or max(ranges[-1][0], l) > min(ranges[-1][1], r):
            ranges.append([l, r])
        else:
            ranges[-1][1] = max(ranges[-1][1], r) 

    l = 0
    for x in q:
        #print(x)
        while l < len(ranges) and not(ranges[l][0] <= x <= ranges[l][1]):  
            #print(x, ranges[l])
            if ranges[l][0] > x:
                break
            l += 1
        if l < len(ranges) and ranges[l][0] <= x <= ranges[l][1]:
            #print(x, ranges[l])
            freshCount += 1

    #print(ranges)
    #print(q)
    print(freshCount)

def second():
    freshCount = 0
    emptySeen = False

    q = []
    for line in lines:
        if line == '':
            emptySeen = True
            continue

        if not emptySeen:
            l, r = map(int, line.split('-'))
            segs.append([l, r]) 

    segs.sort()
    
    ranges = []
    for l, r in segs:
        if len(ranges) == 0 or max(ranges[-1][0], l) > min(ranges[-1][1], r):
            ranges.append([l, r])
        else:
            ranges[-1][1] = max(ranges[-1][1], r) 

    for l, r in ranges:
        freshCount += r - l + 1 
    print(freshCount)

second()
