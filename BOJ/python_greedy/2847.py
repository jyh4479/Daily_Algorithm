num=int(input())
steps=[]
for _ in range(num):
    steps.append(int(input()))

#logic
steps.reverse()
ans=0
for i in range(1,len(steps)):
    if steps[i-1]<=steps[i]:
        ans+=(steps[i]-steps[i-1]+1)
        steps[i]=steps[i-1]-1
print(ans)