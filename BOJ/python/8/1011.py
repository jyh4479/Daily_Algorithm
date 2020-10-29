test_case=int(input())
for _ in range(test_case):
    A,B=map(int,input().split())
    dist=B-A
    num=1
    cnt=1
    while(dist>num**2):
        num+=1
        cnt+=2
    up=num**2
    down=(num-1)**2
    base_line=((down+1)+up)//2
    if(dist<base_line):
        print(cnt-1)
    else:
        print(cnt)