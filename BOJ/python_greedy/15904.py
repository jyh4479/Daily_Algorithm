from collections import deque

word=input()
check=deque(["U","C","P","C"])

for i in word:
    if i==check[0]:
        check.popleft()
    if len(check)==0:
        break

if len(check)==0:
    print("I love UCPC")
else:
    print("I hate UCPC")