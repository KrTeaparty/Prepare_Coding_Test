# 캔디팡
graph = []
for _ in range(7):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, target, cnt):
    if x < 0 or y < 0 or x >= 7 or y >= 7:
        return cnt
    if graph[x][y] == target:
        graph[x][y] = 0
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            res = dfs(nx, ny, target, cnt)
            if res >= cnt:
                cnt = res
        return cnt
    return cnt

result = 0
for i in range(1, 6):
    for x in range(7):
        for y in range(7):
            if dfs(x, y, i, 0) >= 3:
                result += 1

print(result)