#import sys
#
#dy = [0, 0, 1, -1]
#dx = [1, -1, 0, 0]
#ansList = []
#
#
#def dfs(graph, visitGraph, y, x, count):
#    global n, m
#
#    if y == (m - 1) and x == (n - 1):
#        ansList.append(count)
#
#    for i in range(4):
#        ny, nx = dy[i] + y, dx[i] + x
#
#        if ny < 0 or nx < 0 or ny >= m or nx >= n:
#            continue
#
#        if not visitGraph[ny][nx]:
#            visitGraph[ny][nx] = True
#            if graph[ny][nx] == 1:
#                dfs(graph, visitGraph, ny, nx, count + 1)
#            else:
#                dfs(graph, visitGraph, ny, nx, count)
#            visitGraph[ny][nx] = False
#
#
#if __name__ == "__main__":
#    n, m = map(int, sys.stdin.readline().split())
#    graph, visitGraph = [], []
#
#    for _ in range(m):
#        dataList = list(map(int, input()))
#        graph.append(dataList)
#        visitGraph.append([False for _ in range(n)])
#
#    visitGraph[0][0] = True
#    dfs(graph, visitGraph, 0, 0, 0)
#
#    print(min(ansList))
    
    
# 시간초과 DFS풀이


import sys
from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    graph, checkGraph, visitGraph = [], [], []

    for _ in range(m):
        dataList = list(map(int, input()))
        graph.append(dataList)
        visitGraph.append([False for _ in range(n)])
        checkGraph.append([0 for _ in range(n)])

    q = deque()
    q.append((0, 0, 0))

    while q:
        v = q.popleft()
        vy, vx, vCount = v[0], v[1], v[2]

        if not visitGraph[vy][vx]:
            visitGraph[vy][vx] = True

        checkGraph[vy][vx] = vCount

        for i in range(4):
            ny, nx = vy + dy[i], vx + dx[i]
            nCount = vCount

            if ny < 0 or nx < 0 or ny >= m or nx >= n:
                continue

            if graph[ny][nx] == 1:
                nCount += 1

            if not visitGraph[ny][nx] or checkGraph[ny][nx] > nCount:
                q.append((ny, nx, nCount))

    print(checkGraph[n - 1][m - 1])
