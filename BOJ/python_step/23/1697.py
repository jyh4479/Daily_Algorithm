from collections import deque
start,end=map(int,input().split())
visit=[False for _ in range(100001)]
ans=0
q=deque()
q.append([start,ans])
visit[start]=True

while q:
    v=q.popleft() #현재 위치 정보 가져오기
    point=v[0] #위치
    cnt=v[1] #시간
    
    if point==end: #동생을 찾은경우
        ans=cnt
        break
    else:
        if point-1>=0 and visit[point-1]==False:
            visit[point-1]=True
            q.append([point-1,cnt+1])
        if point+1<100001 and visit[point+1]==False:
            visit[point+1]=True
            q.append([point+1,cnt+1])
        if 2*point<100001 and visit[2*point]==False:
            visit[2*point]=True
            q.append([2*point,cnt+1])
print(ans)