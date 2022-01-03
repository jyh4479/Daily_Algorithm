import sys


def search(dataList, L, R, X):
    global nameList
    result = False
    while L <= R:
        mid = (L + R) // 2

        if dataList[mid] < X:
            L = mid + 1
        elif dataList[mid] > X:
            R = mid - 1
        else:
            nameList.append(dataList[mid])
            result = True
            return result
    return result


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    aList, bList = [], []
    nameList = []

    for _ in range(n):
        aList.append(sys.stdin.readline().rstrip("\n"))
    for _ in range(m):
        bList.append(sys.stdin.readline().rstrip("\n"))

    bList.sort()

    ans = 0
    for data in aList:
        if search(bList, 0, len(bList) - 1, data):
            ans += 1

    nameList.sort()
    print(ans)
    for i in nameList:
        print(i)
