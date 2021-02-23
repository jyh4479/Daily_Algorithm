N=int(input())
cnt=0
maps=[list(map(int,input().split())) for _ in range(N)]
visit=[False for _ in range(N)]
man=N//2
############################################# 중복을 줄이기 위한 경우의 개수 미리 계산
cal=0
cal_1=1
cal_2=1
while cnt!=man:
    cal_1*=(N-cnt)
    cnt+=1
cnt=man
while cnt!=0:
    cal_2*=cnt
    cnt-=1
method=(cal_1//cal_2)//2
############################################# 실제로 실행시간 반으로 줄여짐 (백준에서)
min_num=999999

def ans(man_list):
    sum=0
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
    return check

def dfs(idx,cnt,man):
    if cnt==man:
        global min_num, cal, method
        if cal==method:
            return

        min_num=min(min_num,print_list())
        cal+=1
        return
    else:
        for i in range(idx,N):
            if visit[i]==False:
                visit[i]=True
                dfs(i,cnt+1,man)
                visit[i]=False
dfs(0,0,man)
print(min_num)