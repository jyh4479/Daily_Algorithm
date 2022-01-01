import sys

if __name__ == "__main__":
    numberList = []

    n = int(sys.stdin.readline())
    for _ in range(n):
        data = int(sys.stdin.readline())
        numberList.append(data)

    numberList.sort()
    ans = 0
    for i in range(len(numberList)):
        data = numberList[i]
        ans += abs(data - (i + 1))

    print(ans)
