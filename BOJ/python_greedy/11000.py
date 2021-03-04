import heapq
import sys

N = int(input())

timeTable = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
timeTable.sort(key=lambda x: x[0])

queue = []
heapq.heappush(queue,timeTable[0][1])

for i in range(1,N):
    if queue[0] > timeTable[i][0]:
        heapq.heappush(queue,timeTable[i][1])
    else:
        heapq.heappop(queue)
        heapq.heappush(queue,timeTable[i][1])

print(len(queue))