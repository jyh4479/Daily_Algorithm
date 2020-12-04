from collections import deque
def solution(n, edge):
    visit=[False for _ in range(n+1)]
    graph=[list() for _ in range(n+1)]
    ans_list=[0 for _ in range(n)]
    
    for i in edge: #그래프 만들기
        y,x=i[0],i[1]
        graph[y].append(x)
        graph[x].append(y)
        
    q=deque()
    q.append([1,0])
    visit[1]=True
    while q:
        v=q.popleft()
        vertex=v[0]
        dist=v[1]
        ans_list[dist]+=1
        for i in graph[vertex]:
            if visit[i]==False:
                visit[i]=True
                q.append([i,dist+1])
    
    ans=0
    for i in range(len(ans_list)-1,0,-1): #출력을 잘못이해해서 시간이 조금 걸림
        if ans_list[i]!=0:
            ans=ans_list[i]
            break            
    return ans

"""
from collections import deque #거리를 저장하는 방법참고해서 푼 정답
def solution(n, edge):
    visit=[0 for _ in range(n+1)]
    graph=[list() for _ in range(n+1)]
    
    for i in edge: #그래프 만들기
        y,x=i[0],i[1]
        graph[y].append(x)
        graph[x].append(y)
   
    q=deque()
    q.append([1,0])
    visit[1]=-1
    while q:
        v=q.popleft()
        vertex=v[0]
        dist=v[1]
        for i in graph[vertex]:
            if visit[i]==False:
                visit[i]=dist+1
                q.append([i,dist+1])
    ans=0           
    for i in visit:
        if i==max(visit):
            ans+=1
    return ans
"""