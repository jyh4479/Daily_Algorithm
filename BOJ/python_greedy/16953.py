a,b=map(int,input().split())

ans=0
while(a<b):
    if b%10==1: #끝자리 1인경우
        b=(b-1)//10 #1없애기
        ans+=1
    elif b%2==0: #2로 나눠지는 경우
        b=b//2
        ans+=1
    else:
        break

if a==b:
    print(ans+1)
else:
    print(-1)