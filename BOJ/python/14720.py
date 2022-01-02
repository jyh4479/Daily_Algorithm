import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    storeList = list(map(int, sys.stdin.readline().split()))

    ans, start = 0, 0
    for data in storeList:

        # 순서에 맞는 우유 선택시
        if start == data:
            start = (start + 1) % 3
            ans += 1

    print(ans)
