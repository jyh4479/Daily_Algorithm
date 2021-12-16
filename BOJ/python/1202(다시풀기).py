import heapq

if __name__ == '__main__':
    N, K = map(int, input().split())

    itemList = []
    for i in range(N):
        w, p = map(int, input().split())
        itemList.append((w, p))
    itemList = sorted(itemList)

    bagList = []
    for i in range(K):
        bagList.append(int(input()))
    bagList = sorted(bagList)

    hq = []
    for bag in bagList:
        while len(itemList) > 0 and bag >= itemList[0][0]:
            # print(len(itemList))
            heapq.heappush(hq, -itemList[0][1])
            heapq.heappop(itemList)

    ans = 0
    for i in range(K):
        ans += heapq.heappop(hq) * -1

    print(ans)
