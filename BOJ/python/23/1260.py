from collections import deque

v,line,start_idx=map(int,input().split())

graph=[[]for _ in range(v+1)]
visit_DFS=[False for _ in range(v+1)]
visit_BFS=[False for _ in range(v+1)]

def dfs(idx):
    if visit_DFS[idx]==True:
        return
    else:
        visit_DFS[idx]=True #방문 체크
        print(idx,end=" ")

        for i in graph[idx]:
            if visit_DFS[i]==False:
                dfs(i)

def bfs(idx):
    q=deque()
    q.append(idx)

    while q:
        v=q.popleft() #방문
        print(v,end=" ")
        visit_BFS[v]=True #방문 체크

        for i in graph[v]:
            if visit_BFS[i]==False:
                visit_BFS[i]=True
                q.append(i)
    
    

for _ in range(line):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,v+1):
    graph[i].sort()

dfs(start_idx)
print()

bfs(start_idx)
print()