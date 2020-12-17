import sys

def binary(number,start,end,num_list):
    while(start<=end):
        mid=(start+end)//2
        if number==num_list[mid]:
            return 1
        else:
            if number>num_list[mid]:
                start=mid+1
            else:
                end=mid-1
    return 0

num=int(sys.stdin.readline())
num_list=list(map(int,sys.stdin.readline().split()))
num_list.sort() #이진 검색을 위한 정렬

search=int(sys.stdin.readline())
search_list=list(map(int,sys.stdin.readline().split()))

for i in search_list:
    print(binary(i,0,len(num_list)-1,num_list))

"""재귀
import sys

def binary(number,start,end,num_list):
    if start>end:
        return 0
    mid=(start+end)//2
    if num_list[mid]==number:
        return 1
    else:
        if number>num_list[mid]:
            return binary(number,mid+1,end,num_list)
        elif number<num_list[mid]:
            return binary(number,start,mid-1,num_list)
    return 0

num=int(sys.stdin.readline())
num_list=list(map(int,sys.stdin.readline().split()))
num_list.sort() #이진 검색을 위한 정렬

search=int(sys.stdin.readline())
search_list=list(map(int,sys.stdin.readline().split()))

for i in search_list:
    print(binary(i,0,len(num_list)-1,num_list))
"""

"""시간 초과
import sys
num=int(sys.stdin.readline())
num_list=list(map(int,sys.stdin.readline().split()))

search=int(sys.stdin.readline())
search_list=list(map(int,sys.stdin.readline().split()))

for i in search_list:
    if i in num_list:
        print(1)
    else:
        print(0)
"""