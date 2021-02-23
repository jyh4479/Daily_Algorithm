#코팅테스트 책에 개미 전사와 비교해보기 (RGB)
N=int(input())
RGB_list=list()
for _ in range(N):
    RGB_list.append(list(map(int,input().split())))

d=[[0 for _ in range(3)] for _ in range(1000)]

d[0][0],d[0][1],d[0][2]=RGB_list[0][0],RGB_list[0][1],RGB_list[0][2]

for i in range(1,N):
    d[i][0]=RGB_list[i][0]+min(d[i-1][1],d[i-1][2])
    d[i][1]=RGB_list[i][1]+min(d[i-1][0],d[i-1][2])
    d[i][2]=RGB_list[i][2]+min(d[i-1][1],d[i-1][0])

print(min(d[N-1][0],d[N-1][1],d[N-1][2]))