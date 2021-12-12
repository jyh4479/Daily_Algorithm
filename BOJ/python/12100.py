import copy
import sys
from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def checkAns(maps):
    global ans
    for dataList in maps:
        ans = max(ans, max(dataList))


def moveMaps(maps, dict, cnt):
    if cnt == 5:
        checkAns(copy.deepcopy(maps))
        return

    global n
    q = deque()
    # 오른쪽으로 기울이는 경우
    if dict == 0:
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if maps[i][j] != 0:
                    q.append(maps[i][j])
            for j in range(n - 1, -1, -1):
                if len(q) == 0:
                    maps[i][j] = 0
                else:
                    maps[i][j] = q.popleft()
                    if len(q) != 0 and maps[i][j] == q[0]:
                        maps[i][j] += q.popleft()
    # 위로 기울이는 경우
    elif dict == 1:
        for i in range(n):
            for j in range(n):
                if maps[j][i] != 0:
                    q.append(maps[j][i])
            for j in range(n):
                if len(q) == 0:
                    maps[j][i] = 0
                else:
                    maps[j][i] = q.popleft()
                    if len(q) != 0 and maps[j][i] == q[0]:
                        maps[j][i] += q.popleft()

    # 왼쪽으로 기울이는 경우
    elif dict == 2:
        for i in range(n):
            for j in range(n):
                if maps[i][j] != 0:
                    q.append(maps[i][j])
            for j in range(n):
                if len(q) == 0:
                    maps[i][j] = 0
                else:
                    maps[i][j] = q.popleft()
                    if len(q) != 0 and maps[i][j] == q[0]:
                        maps[i][j] += q.popleft()

    # 아래로 기울이는 경우
    elif dict == 3:
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if maps[j][i] != 0:
                    q.append(maps[j][i])
            for j in range(n - 1, -1, -1):
                if len(q) == 0:
                    maps[j][i] = 0
                else:
                    maps[j][i] = q.popleft()
                    if len(q) != 0 and maps[j][i] == q[0]:
                        maps[j][i] += q.popleft()
    for i in range(4):
        moveMaps(copy.deepcopy(maps), i, cnt + 1)


if __name__ == '__main__':
    global n, ans
    n = int(input())
    ans = -sys.maxsize
    maps = []
    for _ in range(n):
        maps.append(list(map(int, input().split())))

    for i in range(4):
        moveMaps(copy.deepcopy(maps), i, 0)

    print(ans)
# 2 2 2
# 4 4 4
# 8 8 8
