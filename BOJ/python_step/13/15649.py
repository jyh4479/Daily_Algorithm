N,M=map(int,input().split())

visit=[False for _ in range(N+1)]
ans=[0 for _ in range(N+1)]
def print_list():
    for i in range(M):
        print(ans[i],end=" ")
    print()

def dfs(idx,num,cnt):
    if cnt == num:
        print_list() 
        return
    else:
        for i in range(1,N+1):
            if visit[i] == False:
                visit[i]=True
                ans[num]=i
                dfs(i,num+1,cnt)
                visit[i]=False
dfs(0,0,M)