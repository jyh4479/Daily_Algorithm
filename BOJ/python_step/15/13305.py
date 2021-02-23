
import sys
input=sys.stdin.readline

N=int(input())
dist=list(map(int,input().split()))
cost=list(map(int,input().split()))

d=[0 for _ in range(len(cost)-1)]

d[0]=cost[0]
for i in range(1,len(d)):
    d[i]=min(d[i-1],cost[i])

ans=0
for i in zip(d,dist):
    ans+=i[0]*i[1]
print(ans)
