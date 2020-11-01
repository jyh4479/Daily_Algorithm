while True:
    arr_num=list(map(int,input().split()))
    arr_num.sort(reverse=True)
    c,b,a=arr_num[0],arr_num[1],arr_num[2]
    if(a==0 and b==0 and c==0):
        break
    else:
        if(a**2+b**2==c**2):
            print("right")
        else:
            print("wrong")