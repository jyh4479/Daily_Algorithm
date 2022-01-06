import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    dataList = []
    for _ in range(n):
        data = int(sys.stdin.readline())
        dataList.append(data)
    dataList = sorted(dataList, reverse=True)

    ans, rank = 0, 1
    for data in dataList:
        result = data - (rank - 1)
        if result < 0:
            break
        ans += result
        rank += 1
    print(ans)
