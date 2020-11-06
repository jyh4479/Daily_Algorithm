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
visited=[False for _ in range(9)]

def dfs(idx):
    visited[idx]=True
    print(idx,end=" ")

    for i in graph[idx]:
        if not visited[i]:
            dfs(i)

dfs(1)

""" 안보고 구현한 DFS
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
visited=[False for _ in range(9)]

def dfs(idx):
    if visited[idx]==True:
        return
    else:
        print(idx,end=" ")
        visited[idx]=True
        for i in graph[idx]:
            dfs(i)

start_idx=1
dfs(start_idx)
print()
"""