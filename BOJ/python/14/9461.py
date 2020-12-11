test_case=int(input())
d=[0]*100
d[0],d[1],d[2]=1,1,1

for i in range(3,100):
    d[i]=d[i-3]+d[i-2]

for _ in range(test_case):
    N=int(input())
    print(d[N-1])