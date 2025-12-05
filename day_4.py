g = open('input.txt', 'r').read().splitlines()
m, n = len(g), len(g[0])
dirs = [[1, -1], [-1, 1], [1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1]]
ans = 0

def first():
    global ans
    for i in range(m):
        for j in range(n):
            if g[i][j] != '@':
                continue
            adjPapers = 0
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                adjPapers += int(g[x][y] == '@')

            ans += int(adjPapers < 4)
    print(ans)

def second():
    global ans

    a = [[-1] * n for _ in range(m)] 
    q, l = [], 0
    adjCount = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if g[i][j] != '@':
                continue
            a[i][j] = 1
            adjPapers = 0
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                adjPapers += int(g[x][y] == '@')

            adjCount[i][j] = adjPapers
            if adjPapers < 4:
                q.append([i, j])

    while l < len(q):
        x, y = q[l] 
        l += 1
        if a[x][y] != 1:
            continue
        a[x][y] = 0 
        ans += 1

        for dx, dy in dirs:
            xx, yy = x + dx, y + dy
            if xx < 0 or xx >= m or yy < 0 or yy >= n or a[xx][yy] != 1:
                continue
            adjCount[xx][yy] -= 1 
            if adjCount[xx][yy] < 4:
                q.append([xx, yy])
     
    print(ans)

second()
