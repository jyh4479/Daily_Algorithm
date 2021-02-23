import sys
#성능을 위해 input대신 sys.stdin.readline 사용
A=input()
for i in range(0,int(A)):
    B,C=sys.stdin.readline().split()
    print(int(B)+int(C))