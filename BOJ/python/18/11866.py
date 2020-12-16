import collections
q=collections.deque()
N,K=map(int,input().split())
ans=list()

for i in range(1,N+1):
    q.append(i)

while q:
    for _ in range(1,K):
        q.append(q.popleft())
    ans.append(q.popleft())

print("<",end="")
for i in range(len(ans)):
    if i==len(ans)-1:
        print(ans[i],end="")
        break
    print(ans[i],end=", ")
print(">")