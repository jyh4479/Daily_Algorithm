N=int(input())
d=[0]*1000000

d[0]=1
d[1]=2
for i in range(2,N):
    d[i]=(d[i-1]+d[i-2])%15746
    #d[i]=(d[i-1]+d[i-2]*2)%15746 --> 처음에 x 2 를했는데 이를 하지 않는 개념을 배움
    #-->http://blog.naver.com/PostView.nhn?blogId=occidere&logNo=220787441430
print(d[N-1])