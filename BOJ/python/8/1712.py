A,B,C=map(int,input().split())
cnt=0
if(B>=C):
    cnt=-1
else:
    cnt=A//(C-B)+1

print(cnt)