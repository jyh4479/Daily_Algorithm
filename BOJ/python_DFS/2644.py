#문제에서 제시한 Data 받기
peopleNumber=int(input())
start,end=map(int,input().split())

#그래프와 방문 체크를 위한 리스트 생성
N=int(input())
graph=[[]for _ in range(peopleNumber+1)]
visit=[False for _ in range(peopleNumber+1)]

ans=-1

def DFS(start,end,cnt):

    if start==end: #도출하기 위한 정점에 닿은경우
        global ans
        ans=cnt
        return

    for i in graph[start]:
        if visit[i]==False: #방문하지 않은경우
            visit[i]=True
            DFS(i,end,cnt+1)
            visit[i]=False

for _ in range(N):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

#DFS logic
visit[start]=True
DFS(start,end,0)
print(ans)
