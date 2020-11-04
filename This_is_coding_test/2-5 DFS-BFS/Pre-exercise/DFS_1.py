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


#재귀로 구현
def dfs(idx):
    if(visited[idx]==False):
        visited[idx]=True
        print(idx,end=" ")
    else:
        for i in range(len(graph[idx])):
            if(visited[graph[idx][i]]==False):
                dfs(graph[idx][i])
            else:
                continue

dfs(1)
print()