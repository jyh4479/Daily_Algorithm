case=1
while True:
    L,P,V=map(int,input().split())
    ans=0
    if L==0 and P==0 and V==0:
        break
    else:
        while(V>0):
            if V>L:
                ans+=L
                V-=P
            else:
                ans+=V
                break
    print("Case {0}: {1}".format(case,ans))
    case+=1