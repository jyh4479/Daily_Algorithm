import heapq

N,M=map(int,input().split())
num_list=list(map(int,input().split()))
heapq.heapify(num_list)

while(M):
    M-=1
    num = heapq.heappop(num_list) + heapq.heappop(num_list)
    heapq.heappush(num_list,num)
    heapq.heappush(num_list,num)

print(sum(num_list))
