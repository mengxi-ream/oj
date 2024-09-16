import sys
import os

LOCAL = os.getenv("LOCAL", "false").lower() == "true"

MAXN = 210
graph = [[" " for _ in range(MAXN)] for _ in range(MAXN)]
row, col = 0, 0


def dfs(r, c):
    global graph, row, col
    if graph[r + 1][c] != "|" or r == row - 1:
        return f"{graph[r][c]}()"
    left, right = c, c
    while left - 1 >= 0 and graph[r + 2][left - 1] == "-":
        left -= 1
    while right + 1 <= col - 1 and graph[r + 2][right + 1] == "-":
        right += 1
    ans = ""
    for i in range(left, right + 1):
        if graph[r + 3][i] != " ":
            ans += dfs(r + 3, i)
    return f"{graph[r][c]}({ans})"


def main():
    global graph, col, row
    cases = int(sys.stdin.readline().strip())
    for _ in range(cases):
        # initial
        graph = [[" " for _ in range(MAXN)] for _ in range(MAXN)]

        col, row = 0, 0
        while True:
            line = list(sys.stdin.readline())[:-1]
            if line[0] == "#":
                break
            for i in range(len(line)):
                graph[row][i] = line[i]
            row += 1
            col = max(col, len(line))

        sc = -1
        for i in range(col):
            if graph[0][i] != " ":
                sc = i
                break
        if sc == -1:
            print("()")
            continue
        print(f"({dfs(0, sc)})")


if __name__ == "__main__":
    if LOCAL:
        sys.stdin = open("uva.in", "r")
        sys.stdout = open("uva.out", "w")
    main()
