import math
a,b=map(int,input().split())

ansA=1
for i in range(b):
    ansA*=(a-i)
print(ansA//math.factorial(b))