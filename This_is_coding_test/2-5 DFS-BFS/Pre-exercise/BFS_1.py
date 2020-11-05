from collections import deque
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
    ]
visit=[False for _ in range(9)]

q=deque()
start_idx=1
q.append(start_idx)
visit[start_idx]=True

while q:
    v=q.popleft()
    print(v,end=" ")

    for i in graph[v]:
        if visit[i]==False:
            q.append(i)
            visit[i]=True
print()