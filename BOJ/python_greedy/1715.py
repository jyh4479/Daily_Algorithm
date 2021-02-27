import heapq

num=int(input())
heap = []

for _ in range(num):
    heapq.heappush(heap,int(input()))

ans=0
while(len(heap)>1):
    sum=heapq.heappop(heap)
    sum+=heapq.heappop(heap)

    ans+=sum
    heapq.heappush(heap,sum)

print(ans)


"""시간초과
num=int(input())

num_list=[]
for _ in range(num):
    num_list.append(int(input()))

num_list=sorted(num_list)

ans=0
while(len(num_list)>1): #존재하면 해당 로직 반복
    sum=0

    sum+=min(num_list)
    num_list.remove(min(num_list))    
    sum+=min(num_list)
    num_list.remove(min(num_list))
    ans+=sum
"""

print(ans)
"""