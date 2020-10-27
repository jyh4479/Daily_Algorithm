num=int(input())
if(num==1):
    print(1)
else:
    cnt=2
    A=2
    B=7
    sum=12
    while True:
        if A<=num<=B:
            print(cnt)
            break
        else:
            cnt+=1
            A=B+1
            B+=sum
            sum+=6