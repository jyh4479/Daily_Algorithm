N,M=map(int,input().split())
coin_list=[]
for _ in range(N):
    coin_list.append(int(input()))

ans_list=[10001 for _ in range(M+1)]
ans_list[0]=0

for coin in coin_list:
    for i in range(coin,M+1):
        if ans_list[i-coin]!=10001:
            ans_list[i]=min(ans_list[i],ans_list[i-coin]+1)
print(ans_list)