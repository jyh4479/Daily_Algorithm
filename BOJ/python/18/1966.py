import collections
test_case=int(input())

for _ in range(test_case):
    N,target=map(int,input().split())
    rank=list(map(int,input().split()))
    q=collections.deque()

    for i in range(N):
        q.append([i,rank[i]])
    max_rank=max(rank)
    
    num=0
    while q:
        i=q.popleft()
        if i[0]==target and i[1]>=max_rank: #정답
            num+=1
            print(num)
            break
        elif max_rank<=i[1]: #출력
            rank.remove(i[1])
            num+=1
            max_rank=max(rank)
        elif max_rank>i[1]: #뒤로보내기
            q.append(i)