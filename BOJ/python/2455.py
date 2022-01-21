if __name__ == "__main__":
    now, ans = 0, 0
    for _ in range(4):
        n, m = map(int, input().split())

        now -= n
        now += m

        ans = max(ans, now)

    print(ans)
