num=int(input())
num_list=list(map(int,input().split()))
cal=list(map(int,input().split()))
cal_list=list()

for i in range(4):#연산 리스트 만들기
    while cal[i]!=0:
        cal_list.append(i)
        cal[i]-=1

visit=[False for _ in range(len(cal_list))]

max_num=-1000000001
min_num=1000000001

def next_num(a,b,cal):
    if cal==0:
        return a+b
    elif cal==1:
        return a-b
    elif cal==2:
        return a*b
    elif cal==3:
        return int(a/b)

def dfs(cnt,ans):
    if cnt==len(num_list):
        global max_num,min_num
        max_num=max(ans,max_num)
        min_num=min(ans,min_num)
        return

    else:
        for i in range(len(cal_list)): #연산 순회
            if visit[i]==False:
                visit[i]=True
                dfs(cnt+1,next_num(ans,num_list[cnt],cal_list[i]))
                visit[i]=False

dfs(1,num_list[0])
print(max_num)
print(min_num)
