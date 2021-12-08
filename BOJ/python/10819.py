import sys


def selNumber(visited, numberList, cnt):
    global ansList, ans
    if cnt == len(numberList):
        sum = 0
        for i in range(len(ansList) - 1):
            sum += abs(ansList[i] - ansList[i + 1])
        ans = max(ans, sum)
    else:
        for i in range(len(visited)):
            if visited[i] == False:
                visited[i] = True
                ansList.append(numberList[i])
                selNumber(visited, numberList, cnt + 1)
                ansList.pop()
                visited[i] = False


if __name__ == '__main__':
    N = int(input())
    ans = - sys.maxsize
    ansList = []

    numberList = list(map(int, input().split()))
    visited = [False for _ in range(len(numberList))]

    selNumber(visited, numberList, 0)
    print(ans)
