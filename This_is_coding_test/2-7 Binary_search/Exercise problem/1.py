#chapter 목적에 맞는 풀이(재귀)
def binary_search(array,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if array[mid]==target:
        return True
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

import sys
N=int(sys.stdin.readline())
item_list=list(map(int,sys.stdin.readline().split()))
s_N=int(sys.stdin.readline())
search_item_list=list(map(int,sys.stdin.readline().split()))
item_list.sort()

for i in search_item_list:
    result=binary_search(item_list,i,0,N-1)
    if result==None:
        print("no",end=" ")
    else:
        print("yes",end=" ")
print()

"""
#내 풀이
import sys
N=int(sys.stdin.readline())
item_list=list(map(int,sys.stdin.readline().split()))
s_N=int(sys.stdin.readline())
search_item_list=list(map(int,sys.stdin.readline().split()))

for i in search_item_list:
    if i in item_list:
        print("yes",end=" ")
    if i not in item_list: #--> else
        print("no",end=" ")
print()
"""