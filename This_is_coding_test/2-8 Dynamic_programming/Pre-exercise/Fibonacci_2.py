N=int(input()) #메모이제이션 사용 --> 속도에서 훨씬 효율적
memo=[0 for _ in range(N+1)]
def F(num):
    if num==1 or num==2:
        return 1
    else:
        if memo[num]!=0:
            return memo[num]
        else:
            memo[num]=F(num-1)+F(num-2)
            return memo[num]

print(F(N))