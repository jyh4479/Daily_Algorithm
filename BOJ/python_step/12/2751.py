import sys
num=int(sys.stdin.readline())
array=[int(sys.stdin.readline()) for _ in range(num)]

for num in sorted(array):
    print(num)