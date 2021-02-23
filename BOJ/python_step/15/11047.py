N,K=map(int,input().split())
bill_list=list()
for _ in range(N):
    bill_list.append(int(input()))
bill_list.sort(reverse=True)

cnt=0
for coin in bill_list:
    if K>=coin:
        cnt+=(K//coin)
        K%=coin
print(cnt)

"""시간 초과
N,K=map(int,input().split())
bill_list=list()
for _ in range(N):
    bill_list.append(int(input()))
bill_list.sort(reverse=True)

cnt=0
for coin in bill_list:
    while K >= coin:
        K-=coin
        cnt+=1
print(cnt)
"""