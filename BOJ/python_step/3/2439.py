A=input()
for i in range(int(A)):
    for j in range(int(A)):
        if(int(A)-j-1<=i):
            print("*",end="")         
        else:
            print(" ",end="")
    print(end="\n")