v=int(input())
line=int(input())

graph=[[]for _ in range(v+1)]
visit=[False for _ in range(v+1)]
cnt=0

def dfs(idx):
    if visit[idx]==True:
        return
    else:
        visit[idx]=True
        for i in graph[idx]:
            if visit[i]==False:
                global cnt
                cnt+=1
                dfs(i)

for _ in range(line): #그래프 생성
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

start_idx=1
dfs(start_idx)
print(cnt)