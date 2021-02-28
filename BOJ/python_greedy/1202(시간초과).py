"""시간초과
N,K=map(int,input().split())

coins=[]
for _ in range(N):
    weight,price=map(int,input().split())
    coins.append([weight, price])

bags=[]
for _ in range(K):
    bags.append(int(input()))

#logic
coins=sorted(coins, key=lambda x:x[1], reverse=True)
bags=sorted(bags)

ans=0
for bag in bags:
    for coin in coins:
        if bag>=coin[0]:
            ans+=coin[1]
            coins.remove(coin)
            break
print(ans)
"""