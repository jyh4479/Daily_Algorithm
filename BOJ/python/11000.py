import heapq

if __name__ == '__main__':
    n = int(input())
    numberList = []
    q = []
    for _ in range(n):
        a, b = map(int, input().split())
        numberList.append((a, b))
    numberList.sort()

    heapq.heappush(q, numberList[0][1])
    for i in range(1, len(numberList)):
        # 강의실 교체
        if numberList[i][0] >= q[0]:
            heapq.heappop(q)
            heapq.heappush(q, numberList[i][1])
        # 강의실 추가
        else:
            heapq.heappush(q, numberList[i][1])

    print(len(q))
