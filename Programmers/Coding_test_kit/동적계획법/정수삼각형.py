def solution(triangle):
    d=[[0 for _ in range(len(triangle))]for _ in range(len(triangle))]
    d[0][0]=triangle[0][0]

    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j==0:#제일 왼쪽인 경우
                d[i][j]=triangle[i][j]+d[i-1][j]
            elif j==len(triangle[i])-1:#제일 오른쪽인 경우
                d[i][j]=triangle[i][j]+d[i-1][j-1]
            else:#양쪽 다 있는 경우
                d[i][j]=triangle[i][j]+max(d[i-1][j],d[i-1][j-1])

    answer = max(d[len(triangle)-1])
    return answer