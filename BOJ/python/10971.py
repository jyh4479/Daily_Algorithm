import sys


def dfs(visited, costList, start, cnt, checkList):
    global n, sumCost, ans

    if cnt == n - 1:
        last = checkList[-1]
        for data in costList[last]:
            if data[0] == 0:
                ans = min(ans, sumCost + data[1])
    else:
        for data in costList[start]:
            next, cost = data[0], data[1]
            if visited[next] == False:
                visited[next] = True
                checkList.append(next)
                sumCost += cost
                dfs(visited, costList, next, cnt + 1, checkList)
                sumCost -= cost
                checkList.pop()
                visited[next] = False


if __name__ == '__main__':
    global n, sumCost, ans
    n = int(input())
    sumCost, ans = 0, sys.maxsize

    costList = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    checkList = []

    for i in range(n):
        dataList = list(map(int, input().split()))
        for j in range(n):
            if dataList[j] != 0:
                costList[i].append((j, dataList[j]))

    visited[0] = True
    checkList.append(0)
    dfs(visited, costList, 0, 0, checkList)

    # print(costList)
    print(ans)
