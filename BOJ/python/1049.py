import sys

if __name__ == "__main__":
    wire, m = map(int, sys.stdin.readline().split())
    setCost, oneCost = sys.maxsize, sys.maxsize

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        setCost, oneCost = min(setCost, a), min(oneCost, b)

    ans = 0
    if setCost == 0 or oneCost == 0:
        ans = 0
    else:
        a = ((wire // 6) * setCost) + ((wire % 6) * oneCost)
        b = wire * oneCost
        c = ((wire // 6) * setCost) + setCost

        ans = min(a, b, c)

    print(ans)
