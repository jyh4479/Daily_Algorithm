import sys

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    k = int(sys.stdin.readline())
    numberList, homeList = [], [m for _ in range(n)]

    for _ in range(k):
        a, b, c = map(int, sys.stdin.readline().split())
        numberList.append((a - 1, b - 1, c))

    numberList = sorted(numberList, key=lambda x: x[1])

    ans = 0
    for data in numberList:
        start, end, count = data

        # 경유하는 마을에서 이동시킬 수 있는 박스의 개수
        canMove = min(homeList[start:end])
        canMove = min(canMove, count)

        for i in range(start, end):
            homeList[i] -= canMove

        ans += canMove

    print(ans)
