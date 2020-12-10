N=int(input())
d=[0]*30001

for i in range(2,N+1): #조건의 순서가 중요한 이유는 비효율적인 해부터 저장한 후 최적의 해를 찾는 과정을 만들기 위함이다
    d[i]=d[i-1]+1
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)
    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)
    if i%5==0:
        d[i]=min(d[i],d[i//5]+1)
print(d[N])
