from collections import deque

M, N, K, X = map(int, input().split())
graph = [[] for _ in range(M + 1)]
ans = list()
for _ in range(N):
    x, y = map(int, input().split())
    graph[x].append(y)

visit = [False for _ in range(M + 1)]
start, visit[X] = X, True
q = deque()
q.append([start, 0])

while q:
    v = q.popleft()
    check, dist = v[0], v[1]
    for i in graph[check]:
        if not visit[i]:
            visit[i] = True
            q.append([i, dist + 1])
            if dist + 1 == K:
                ans.append(i)

if not ans:
    print(-1)
else:
    for data in ans:
        print(data)
