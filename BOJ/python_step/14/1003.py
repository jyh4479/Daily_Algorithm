memo=[[1,0]]
for i in range(1,41):
    memo.append([memo[i-1][1],sum(memo[i-1])])

N=int(input())
for _ in range(N):
    num=int(input())
    print(memo[num][0],memo[num][1])