import sys


def search(l, r, x, numberList, checkList):
    while l <= r:
        mid = (l + r) // 2
        if numberList[mid] < x:
            l = mid + 1
            continue
        elif numberList[mid] > x:
            r = mid - 1
            continue
        else:
            return True
    return False


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    numberList = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    checkList = list(map(int, sys.stdin.readline().split()))
    numberList.sort()

    ansList = []
    for data in checkList:
        if search(0, len(numberList) - 1, data, numberList, checkList):
            ansList.append(1)
        else:
            ansList.append(0)

    for ans in ansList:
        print(ans, end=" ")
    print()
