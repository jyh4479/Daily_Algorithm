if __name__ == "__main__":
    n, ans = map(int, input().split())
    numberList = list(map(int, input().split()))
    numberList.sort()
    for data in numberList:
        if data <= ans:
            ans += 1
        else:
            break
    print(ans)
