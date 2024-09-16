from collections import deque
from collections import defaultdict


def findCheapestPrice(n, flights, src, dst, k):
    f = [[float('inf') for _ in range(k + 2)] for _ in range(n)]
    visit = [0 for _ in range(n)]
    graph = [[] for _ in range(n)]

    for flight in flights:
        graph[flight[0]].append((flight[1], flight[2]))

    def dfs(u):
        if u == dst:
            f[dst][0] = 0
            visit[dst] = 1
            return
        visit[u] = -1

        for node in graph[u]:
            v, p = node
            if visit[v] == -1:
                continue
            if visit[v] == 0:
                dfs(v)
            for i in range(k + 1):
                if f[v][i] != float('inf') :
                    f[u][i + 1] = min(f[u][i + 1], p + f[v][i])

        visit[u] = 1

    dfs(src)

    # print ans
    ans = float("inf")
    for i in range(k + 2):
        if f[src][i] != float('inf'):
            ans = min(ans, f[src][i])

    return -1 if ans == float("inf") else ans


print(
    findCheapestPrice(
        10,
        [
            [3, 4, 4],
            [2, 5, 6],
            [4, 7, 10],
            [9, 6, 5],
            [7, 4, 4],
            [6, 2, 10],
            [6, 8, 6],
            [7, 9, 4],
            [1, 5, 4],
            [1, 0, 4],
            [9, 7, 3],
            [7, 0, 5],
            [6, 5, 8],
            [1, 7, 6],
            [4, 0, 9],
            [5, 9, 1],
            [8, 7, 3],
            [1, 2, 6],
            [4, 1, 5],
            [5, 2, 4],
            [1, 9, 1],
            [7, 8, 10],
            [0, 4, 2],
            [7, 2, 8],
        ],
        6,
        0,
        7,
    )
)
