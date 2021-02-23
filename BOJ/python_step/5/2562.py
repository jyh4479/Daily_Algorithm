arr=[]
max_num=-1000000
loc=0
while True:
    try:
        a=int(input())
        arr.append(a)
    except:
        for i in range(len(arr)):
            max_num=max(max_num,arr[i])
            if(arr[loc]!=max_num):
                loc=i
        break;
print(max_num)
print(loc+1)