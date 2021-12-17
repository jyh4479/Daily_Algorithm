from collections import deque


def solution(rows, columns, queries):
    maps = []
    start = 1
    for i in range(rows):
        maps.append([i for i in range(start, columns + start)])
        start += columns

    ans = []
    for data in queries:
        sy, sx, ey, ex = data[0] - 1, data[1] - 1, data[2] - 1, data[3] - 1
        q = deque()

        # 시계돌리기 시작
        # 오른쪽
        for i in range(sx, ex + 1):
            q.append(maps[sy][i])
        # 아래쪽
        for i in range(sy + 1, ey + 1):
            q.append(maps[i][ex])
        # 왼쪽
        for i in range(ex - 1, sx - 1, -1):
            q.append(maps[ey][i])
        # 위쪽
        for i in range(ey - 1, sy, -1):
            q.append(maps[i][sx])

        ans.append(min(q))
        ##################################

        # 값 재배치
        for i in range(sx + 1, ex + 1):
            maps[sy][i] = q.popleft()
        # 아래쪽
        for i in range(sy + 1, ey + 1):
            maps[i][ex] = q.popleft()
        # 왼쪽
        for i in range(ex - 1, sx - 1, -1):
            maps[ey][i] = q.popleft()
        # 위쪽
        for i in range(ey - 1, sy - 1, -1):
            maps[i][sx] = q.popleft()

    return ans
