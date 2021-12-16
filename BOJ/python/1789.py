if __name__ == '__main__':
    number = int(input())

    ans, start, sum = 1, 1, 1

    while sum < number:
        start += 1
        sum += start
        ans += 1

    if sum != number:
        print(ans - 1)
    else:
        print(ans)
