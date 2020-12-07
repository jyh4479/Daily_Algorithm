N,K=map(int,input().split())
list_A=list(map(int,input().split()))
list_B=list(map(int,input().split()))

#원래 의도 코드
list_A.sort()
list_B.sort(reverse=True)
for i in range(K):
    if list_A[i]<list_B[i]:
        list_A[i],list_B[i]=list_B[i],list_A[i]
print(sum(list_A))

#정렬 없이 구현 --> 시간초과예상됌
"""
for _ in range(K):
    if min(list_A)<max(list_B):
        list_A.append(max(list_B))
        list_A.remove(min(list_A))
        list_B.remove(max(list_B))
print(sum(list_A))
"""
