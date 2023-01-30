# Up 2

m, n = map(int, input().split())

graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

answer = dict()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, i, cnt):
    if x < 0 or y < 0 or x >= m or y >= n:
        return cnt
    if graph[x][y] == i:
        graph[x][y] = -2
        cnt += 1
        for j in range(4):
            result = dfs(x + dx[j], y + dy[j], i, cnt)
            if result >= cnt:
                cnt = result
        return cnt
    return cnt

# 0~9까지 반복
for i in range(10):
    result = 0
    # 모든 노드에 대해 반복
    for x in range(m):
        for y in range(n):
            result = dfs(x, y, i, 0)
            # 탐색 결과 0 이상이고, answer에 존재하지 않는다면 등록
            if (i not in answer) and (result > 0):
                answer[i] = result
                continue
            # answer에 존재하고, 기존의 결과보다 크다면 교체
            if (i in answer) and (result > answer[i]):
                answer[i] = result
            
result = list(zip(answer.keys(), answer.values()))
result = sorted(result, key=lambda x:x[0], reverse=False)
for key, value in result:
    if key != -1:
        print(key, value)
