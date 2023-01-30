# 숫자 등고선
from collections import deque

# 배열 크기 N
n = int(input())
# 시작 위치 X, Y
x, y = map(int, input().split())

graph = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x-1, y-1))
    graph[x-1][y-1] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >=n or ny >= n:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    for i in range(n):
        for j in range(n):
            print(graph[i][j], end=' ')
        print()

bfs(x, y)