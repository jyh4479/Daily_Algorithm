from collections import deque #라이브러리 주목

queue=deque()

queue.append(2)
queue.append(4)
queue.append(5)
queue.append(7)
queue.append(1)
queue.popleft()
queue.append(2)
queue.append(4)
queue.popleft()
#queue.pop() --> stack과 똑같이 사용가능

print(queue) #출력 주목
queue.reverse()
print(queue)