test_case=int(input())
for _ in range(test_case):
    k=int(input())
    n=int(input())
    room=[[i for i in range(1,15)] for _ in range(15)]

    for i in range(1,15):
        sum=0
        for j in range(14):
            sum+=room[i-1][j]
            room[i][j]=sum
    print(room[k][n-1])