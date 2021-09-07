def first_binary(array,target,start,end):
    if start>end:
        return None
    
    mid=(start+end)//2
    if (mid==0 or array[mid-1]<target) and array[mid]==target:
        return mid
    elif array[mid]>=target:
        return first_binary(array,target,start,mid-1)
    else:
        return first_binary(array,target,mid+1,end)

def second_binary(array,target,start,end):
    if start>end:
        return None
        
    mid=(start+end)//2
    if (mid==n-1 or array[mid+1]>target) and array[mid]==target:
        return mid
    elif array[mid]>target:
        return second_binary(array,target,start,mid-1)
    else:
        return second_binary(array,target,mid+1,end)

def count_value(array,target):
    n=len(array)

    a=first_binary(array,target,0,n-1)

    if a==None:
        return None

    b=second_binary(array,target,0,n-1)

    return b-a+1

n,target=map(int,input().split())
array=list(map(int,input().split()))

ans=count_value(array,target)

if ans == None:
    print(-1)
else:
    print(ans)
