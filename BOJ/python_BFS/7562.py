from collections import deque

N=int(input())

def bfs(starty,startx,endy,endx,size,graph):
    dicty=[1,-1,1,-1,2,-2,2,-2]
    dictx=[2,2,-2,-2,1,1,-1,-1]

    q=deque()
    q.append([starty,startx])
    while(q):
        v=q.popleft()

        if v[0]==endy and v[1]==endx:
            return graph[endy][endx]

        for i in range(8):
            dy=v[0]+dicty[i]
            dx=v[1]+dictx[i]
            if dy<0 or dx<0 or dy>=size or dx>=size or graph[dy][dx]!=0:
                continue
            else:
                graph[dy][dx]=graph[v[0]][v[1]]+1
                q.append([dy,dx])

for _ in range(N):
    size=int(input()) #그래프의 크기
    starty,startx=map(int,input().split()) #시작점, 끝점
    endy,endx=map(int,input().split()) #시작점, 끝점

    graph=[[0 for _ in range(size)] for _ in range(size)]
    print(bfs(starty,startx,endy,endx,size,graph))