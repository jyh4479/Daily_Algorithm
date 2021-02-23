num=int(input())
ans=0
for i in range(1,num+1):
    cal=i
    if(i<100):
        ans+=1
    elif(i==1000):
        ans+=0
    else:#3자리수
        a=cal%10
        cal//=10
        b=cal%10
        cal//=10
        c=cal%10
        if((b-c)==(a-b)):
            ans+=1
print(ans)