if __name__ == '__main__':
    N = int(input())
    ListA = list(map(int, input().split()))
    ListB = list(map(int, input().split()))

    ListA = sorted(ListA)
    ListB = sorted(ListB, reverse=True)

    ans = 0
    for i in range(N):
        ans += ListA[i] * ListB[i]

    print(ans)
