arr=[0 for _ in range(15000)]

def sol(num):
    sum=num
    while(num>0):
        sum+=(num%10)
        num//=10
    return sum

for i in range(10001):
    arr[sol(i)]=1
for i in range(10001):
    if(arr[i]!=1):
        print(i)