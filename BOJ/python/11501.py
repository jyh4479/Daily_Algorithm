import sys

if __name__ == "__main__":
    testCase = int(sys.stdin.readline())

    ansList = []
    for _ in range(testCase):
        n = int(sys.stdin.readline())
        numberList = list(map(int, sys.stdin.readline().split()))

        ans = 0
        curPrice = numberList[len(numberList) - 1]
        for i in range(len(numberList) - 2, -1, -1):
            price = numberList[i]

            # 구매
            if price < curPrice:
                ans += (curPrice - price)
            # 관망
            elif price >= curPrice:
                curPrice = price

        ansList.append(ans)

    for ans in ansList:
        print(ans)
