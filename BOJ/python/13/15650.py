N,M=map(int,input().split())
visit=[False for _ in range(N)]

def print_list():
    for i in range(N):
        if visit[i]==True:
            print(i+1,end=" ")
    print()

def dfs(idx,num,cnt):
    if cnt == num:
        print_list() 
        return
    else:
        for i in range(idx,N):
            if visit[i] == False:
                visit[i]=True
                dfs(i,num+1,cnt)
                visit[i]=False
dfs(0,0,M)