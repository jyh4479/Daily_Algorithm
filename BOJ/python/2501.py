if __name__ == '__main__':
    N, K = map(int, input().split())
    numberList = [0 for _ in range(N + 1)]

    check = 1
    for i in range(1, N + 1):
        if N % i == 0:
            numberList[check] = i
            check += 1
    print(numberList[K])
