import sys
input=sys.stdin.readline
INF=int(1e9)
n=int(input())
m=int(input())

graph=[[INF for _ in range(n+1)]for _ in range(n+1)]
for i in range(n+1): #대각선 초기화
    graph[i][i]=0

for _ in range(m): #간선 정보
    a,b,c=map(int,input().split())
    graph[a][b]=c

for k in range(1,n+1): #플로이드워셜 알고리즘
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,n+1):
    print(graph[i][1:])
"""
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
"""