import sys
N, S = map(int, input().split())
numbers=list(map(int,input().split()))


start, end, ans = 0, 0, sys.maxsize
sum=numbers[start]
while True:
    if sum>=S:
        ans=min(ans,end-start+1)

    if sum < S and end!=N:
        end+=1
        if end == N:
            break
        sum+=numbers[end]
        
    else:
        sum-=numbers[start]
        start+=1

   


if sys.maxsize == ans:
    ans=0
print(ans)
