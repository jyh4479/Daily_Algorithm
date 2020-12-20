#N이 1 or 2인 경우 예외처리 해주어야함
N=int(input())
array=[]
for _ in range(N):
    array.append(int(input()))

if N==1:
    print(array[0])
elif N==2:
    print(max(array[1],array[0]+array[1]))
else:
    d=[0]*301
    d[0]=array[0]
    d[1]=max(array[1],array[0]+array[1])
    d[2]=max(array[0]+array[2],array[1]+array[2])


    for i in range(3,N):
        d[i]=max(array[i]+d[i-2],array[i]+array[i-1]+d[i-3]) #전칸에서 오는 경우 d[i-1]+array[i]를 하게 되면 연속으로 세개 못밟는 조건을 위배하게 됌

    print(d[N-1])