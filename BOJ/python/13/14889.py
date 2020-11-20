N=int(input())
maps=[list(map(int,input().split())) for _ in range(N)]
visit=[False for _ in range(N)]
man=N//2
min_num=999999

def ans(man_list):
    sum=0
    #print(man_list)
    for i in range(len(man_list)-1):
        for j in range(i+1,len(man_list)):
            sum+=maps[man_list[i]][man_list[j]]+maps[man_list[j]][man_list[i]]
    return sum

def print_list():
    start_team=[]
    link_team=[]
    for i in range(N):
        if visit[i]==True:
            start_team.append(i)
        elif visit[i]==False:
            link_team.append(i)
    check=abs(ans(start_team)-ans(link_team))
    #print(check)
    return check

def dfs(idx,cnt,man):
    if cnt==man:
        global min_num
        min_num=min(min_num,print_list())
        return
    else:
        for i in range(idx,N):
            if visit[i]==False:
                visit[i]=True
                dfs(i,cnt+1,man)
                visit[i]=False
dfs(0,0,man)
print(min_num)