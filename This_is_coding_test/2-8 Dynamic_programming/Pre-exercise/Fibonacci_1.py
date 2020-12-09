#일반 재귀 피보나치
N=int(input())

def F(num):
    if num==1 or num==2:
        return 1
    else:
        return F(num-1)+F(num-2)

print(F(N))