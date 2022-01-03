import sys


def solve(numberList, X):
    L, R = 0, len(numberList) - 1
    result = 0

    while L <= R:
        mid = (L + R) // 2
        if numberList[mid] >= X:
            R = mid - 1
        else:
            L = mid + 1

    start = L
    number = X
    while start < len(numberList) and number == numberList[start]:
        result += 1
        start += 1

    return result


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    numberList = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    checkList = list(map(int, sys.stdin.readline().split()))

    numberList.sort()

    for data in checkList:
        ans = solve(numberList, data)
        print(ans, end=" ")
    print()
    
# python3, pypy3 시간초과
