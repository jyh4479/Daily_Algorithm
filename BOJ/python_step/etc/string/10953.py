N=int(input())

for _ in range(N):
    string=str(input())
    print(int(string[0])+int(string[2]))

"""숫자 제한이 없는경우 (응용)
N=int(input())

for _ in range(N):
    string=list(input().split(','))
    print(string)
    print(sum(list(map(int,string))))
"""