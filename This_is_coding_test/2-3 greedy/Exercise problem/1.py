N,M,K=map(int,input().split())
arr=input().split()
#--> data=list(map(int, input().split()))

i_arr=[]
for i in range(N):
    i_arr.append(int(arr[i]))
i_arr.sort()
ans=0
for i in range(1,M+1):
    if(i%K!=0):
        ans+=i_arr[N-1]
    elif(i%K==0):
        ans+=i_arr[N-2]
print(ans)