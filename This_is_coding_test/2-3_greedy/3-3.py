A,B=map(int,input().split())
max_num=0
for i in range(A):
    min_num=9999
    arr=list(map(int,input().split()))
    for j in range(B):
        min_num=min(min_num,arr[j])
    max_num=max(max_num,min_num)
print(max_num)