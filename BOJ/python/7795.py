import sys


def search(dataList, start, end, x):
    result = start - 1
    while start <= end:
        mid = (start + end) // 2

        if dataList[mid] < x:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result


if __name__ == "__main__":
    n = int(sys.stdin.readline())

    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        aList = list(map(int, sys.stdin.readline().split()))
        bList = list(map(int, sys.stdin.readline().split()))
        bList.sort()

        ans = 0
        for i in aList:
            ans += search(bList, 0, len(bList) - 1, i) + 1

        print(ans)
