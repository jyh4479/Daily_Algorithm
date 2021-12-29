from collections import deque


def outCode(inputList, codeList, data, start):
    global m
    q = deque()
    checkList = [0] * (m + 1)

    for i in range(start, len(inputList)):
        input = inputList[i]
        if input not in q:
            q.appendleft(input)

    for i in range(len(codeList)):
        input = codeList[i]
        if input not in q:
            codeList[i] = data
            return

    select = 0
    while q:
        if q[0] in codeList:
            select = q[0]
            break
        else:
            q.popleft()

    for i in range(len(codeList)):
        input = codeList[i]
        if input == select:
            codeList[i] = data
            return


def canInCheck(codeList, data):
    for i in range(len(codeList)):
        if codeList[i] == 0:
            codeList[i] = data
            return True
    return False


if __name__ == '__main__':
    global m
    n, m = map(int, input().split())
    inputList = list(map(int, input().split()))
    codeList = [0] * n
    ans = 0

    for i in range(len(inputList)):
        data = inputList[i]
        if data in codeList:
            continue
        elif canInCheck(codeList, data):
            continue
        else:  # 코드 빼야하는경우
            ans += 1
            if i + 1 >= len(inputList):
                break
            outCode(inputList, codeList, data, i + 1)
    print(ans)
