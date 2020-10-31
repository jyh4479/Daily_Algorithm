num=map(int,input())
arr=list(map(int,input().split()))

cnt=0
def search(number):
    if(number==1):
        return 0
    for j in range(2,((number//2)+1)):
        if(number%j==0):
            return 0
    return 1

for i in range(len(arr)):
    cnt+=search(arr[i])

print(cnt)