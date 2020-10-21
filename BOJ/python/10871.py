"""
A,B=input().split()
C=input().split()

for i in range(0,int(A)):
    if(int(C[i])<int(B)):
        print(int(C[i]),end=" ")
print("\n")
참고:https://blog.naver.com/wpghks7/221584113312
"""

A,B=input().split()
C=list(map(int,input().split()))

for i in range(0,int(A)):
    if(C[i]<int(B)):
        print(C[i],end=" ")
print("\n")