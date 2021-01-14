import sys
import heapq
input=sys.stdin.readline
N=int(input())
num_list=[]
for _ in range(N):
    cmd=int(input())
    if cmd==0:
        if len(num_list)==0:
            print(0)
        else:
            print(heapq.heappop(num_list)[1])
    else:
        heapq.heappush(num_list,(-cmd,cmd))

"""힙으로 해결안하면 시간초과
import sys
input=sys.stdin.readline
N=int(input())
num_list=[]
for _ in range(N):
    cmd=int(input())
    if cmd==0:
        if len(num_list)==0:
            print(0)
        else:
            print(max(num_list))
            num_list.remove(max(num_list))
    else:
        num_list.append(cmd)
"""