line = open('input2.txt', 'r').read()
nums = list(map(lambda str: list(map(int, str.split('-'))), line.split(',')))
answer = 0
counter = [0] * 10

divs = [[] for _ in range(12)]
for i in range(1, 12):
    div = 1
    for j in range(2*i, 12, i):
        div = div * 10**i + 1
        divs[j].append(div)
for i in divs:
    print(i)

for l, r in nums:
    for i in range(l, r + 1):
        l = len(str(i))
        for div in divs[l]:
            if i % div == 0:
                answer += i
                print(i)
                break
    # print(l, r)
print(answer)