N,M=map(int,input().split())
visit=[0 for _ in range(N)]

def print_list():
    for i in range(M):
        print(visit[i]+1,end=" ")
    print()

def dfs(idx,num,cnt):
    if cnt == num:
        print_list() 
        return
    else:
        for i in range(idx,N):
            visit[num]=i
            dfs(i,num+1,cnt)
dfs(0,0,M)