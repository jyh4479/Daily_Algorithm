N=int(input())

while N!=1:
    for num in range(2,N+1):
        while N%num==0:
            print(num)
            N//=num

"""
N=int(input())

while N!=1:
    for num in range(2,N+1):
        if N%num==0:
            print(num)
            N//=num
            break
#효율적이게 다시 풀어보기
"""