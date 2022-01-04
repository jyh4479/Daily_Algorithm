import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    numberList = []
    ansList = [0] * 1001

    for _ in range(n):
        d, w = map(int, sys.stdin.readline().split())
        numberList.append((d, w))

    numberList = sorted(numberList, key=lambda x: (x[1], x[0]), reverse=True)

    for data in numberList:
        d, w = data[0], data[1]
        for i in range(d, 0, -1):
            if ansList[i] == 0:
                ansList[i] = w
                break

    print(sum(ansList))
