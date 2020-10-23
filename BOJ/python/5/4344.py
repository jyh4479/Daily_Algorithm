num=int(input())
for i in range(num):
    A=input().split()
    cnt=int(A[0])
    arr=A[1:len(A)]
    sum=0
    for i in range(len(arr)):
        sum+=int(arr[i])
    avg=sum/cnt
    over=0
    for i in range(len(arr)):
        if(avg<int(arr[i])):
            over+=1
    ans=(over/cnt)*100
    print("{0:.3f}%".format(round(ans,3)))
    #참고: https://tariat.tistory.com/823