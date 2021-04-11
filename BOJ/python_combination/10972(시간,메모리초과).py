import copy
import sys
sys.setrecursionlimit(100000)
N=int(input())
checkList=list(map(int,input().split()))
visit=[False for _ in range(N)]
numList=[]
ansList=[]

def check(a,b):
    for i in range(len(a)):
        if a[i]!=b[i]:
            return False
    return True

def dfs(idx,cnt,sel):
    if cnt==sel:
        copyList=copy.deepcopy(numList)
        ansList.append(copyList)
    else:
        for i in range(N):
            if visit[i]==False:
                visit[i]=True
                numList.append(i+1)
                dfs(i,cnt+1,sel)
                numList.pop()
                visit[i]=False

dfs(0,0,N)
for i in range(len(ansList)):
    if i==len(ansList)-1:
        print(-1)
        break
    if check(ansList[i],checkList)==True:
        for j in ansList[i+1]:
            print(j,end=" ")
        print()
        break