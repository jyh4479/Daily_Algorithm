A,B=input().split()
A=int(A)
B=int(B)
if(B<45):
    B+=60
    B-=45
    if(A==0):
        A=23
    else:
        A-=1
elif(B>=45):
    B-=45
print(A, B)