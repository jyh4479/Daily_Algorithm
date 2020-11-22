import sys
num=int(sys.stdin.readline())
array=[0 for _ in range(10001)]

for _ in range(num):
    number=int(sys.stdin.readline())
    array[number]+=1
for i in range(10001):
    for j in range(array[i]):
        print(i)