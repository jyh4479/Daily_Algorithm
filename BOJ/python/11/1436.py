num=int(input())

compare=666
ans=0
while(num>0):
    number=str(compare)
    cnt=0
    for i in range(len(number)-1,-1,-1):
        if(number[i]=="6"):
            cnt+=1
        if(number[i]!="6"):
            cnt=0
        if(cnt==3):
            num-=1
            ans=compare
            break
    compare+=1
print(ans)