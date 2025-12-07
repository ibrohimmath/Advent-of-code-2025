lines = open("input.txt", "r").read().splitlines()

def first():
    # matrix
    g = list(map(lambda line: list(line), lines))
    m, n = len(g), len(g[0])

    # matrix iterating index
    raw = 0

    # split count
    splitCount = 0

    # queue
    l = 0
    q = []

    while raw < len(g):
        if raw == 0:
            c = g[0].index('S')
            q.append([0, c])
        else:
            while l < len(q) and q[l][0] <= raw - 1:
                x, y = q[l]
                l += 1

                if x < raw - 1 or (g[x][y] != '.' and g[x][y] != 'S'):
                    continue
                g[x][y] = '|'

                # straight go down
                if g[x + 1][y] == '.':
                    q.append([x + 1, y])
                elif g[x + 1][y] == '^':
                    splitCount += 1
                    for dy in [-1, 1]:
                        yy = y + dy
                        if yy < 0 or yy >= n or g[x + 1][yy] != '.':
                            continue
                        q.append([x + 1, yy])
        raw += 1

    print(splitCount)

def second():
    # matrix
    g = list(map(lambda line: list(line), lines))
    m, n = len(g), len(g[0])

    dp = [0] * n

    # matrix iterating index
    raw = 0

    # split count
    splitCount = 0

    while raw < len(g):
        if raw == 0:
            c = g[0].index('S')
            dp[c] = 1
        else:
            prev = dp.copy()
            dp = [0] * n

            # raw-th index in g
            for j in range(n):
                if g[raw][j] == '.':
                    for dc in [-1, 0, 1]:
                        jj = j + dc
                        if jj < 0 or jj >= n: 
                            continue  
                        if jj == j and (g[raw - 1][jj] == '|' or g[raw - 1][jj] == 'S'):
                            dp[j] += prev[jj]
                        elif jj != j and g[raw][jj] == '^':
                            dp[j] += prev[jj] 
                    g[raw][j] = '|'
        raw += 1

    print(sum(dp))

second()