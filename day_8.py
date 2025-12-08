from functools import reduce

lines = open("input.txt", "r").read().splitlines()

N = 1001

class DSU:
    def __init__(self, n: int):
        self.par = [i for i in range(n)] 
        self.sz = [1] * n 

    def find_set(self, u: int) -> int:
        if self.par[u] == u:
            return u
        self.par[u] = self.find_set(self.par[u])
        return self.par[u]

    def union_sets(self, u: int, v: int) -> tuple[int]:
        ans = [u, v]

        # print(u, v)
        u = self.find_set(u)
        v = self.find_set(v)
        if u == v:
            return [-1, -1] 

        if self.sz[u] < self.sz[v]:
            u, v = v, u
        self.sz[u] += self.sz[v]
        self.par[v] = u

        # print(u, v)
        # print(self.sz[u], self.sz[v])

        return ans

def first():
    dsu = DSU(N)

    nodes = []
    for line in lines:
        x, y, z = map(int, line.split(','))
        nodes.append((x, y, z))

    edges = []
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            dist = 0
            for k in range(3):
                dist += (nodes[i][k] - nodes[j][k]) ** 2
            edges.append((dist, i, j))

    edges.sort()
    conn = 0
    for _, i, j in edges:
        # if conn == 1000:
        #     break
        # print(nodes[i], nodes[j])
        dsu.union_sets(i, j)
        conn += 1

    dsu.sz.sort(reverse=True)
    print(reduce(lambda x, y: x * y, dsu.sz[0:3]))

def second():
    dsu = DSU(N)

    nodes = []
    for line in lines:
        x, y, z = map(int, line.split(','))
        nodes.append((x, y, z))

    edges = []
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            dist = 0
            for k in range(3):
                dist += (nodes[i][k] - nodes[j][k]) ** 2
            edges.append((dist, i, j))

    edges.sort()
    last = 0
    for _, i, j in edges:
        [u, v] = dsu.union_sets(i, j)
        if u != -1 and v != -1:
            last = nodes[u][0] * nodes[v][0]

    print(last)

second()