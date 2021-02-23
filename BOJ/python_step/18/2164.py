import collections
N=int(input())
q=collections.deque([i+1 for i in range(N)])

while len(q)>1:
    q.popleft()#버리기
    q.append(q.popleft())#아래로 넣기

print(q.popleft())