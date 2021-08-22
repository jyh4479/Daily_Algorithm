import sys

number = list(map(int, input()))

result = sys.maxsize
for i in range(2):
    count, prev = 0, 2
    for data in number:
        if data == i and data != prev:
            count = count + 1
        prev = data
    result = min(result, count)

print(result)
