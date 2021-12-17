if __name__ == '__main__':
    n, m = input().split()
    n = list(n)
    m = list(m)

    for i in range(len(n)):
        if n[i] == '5': n[i] = '6'
    for j in range(len(m)):
        if m[j] == '5': m[j] = '6'

    ans_max = int("".join(n)) + int("".join(m))

    for i in range(len(n)):
        if n[i] == '6': n[i] = '5'
    for j in range(len(m)):
        if m[j] == '6': m[j] = '5'

    ans_min = int("".join(n)) + int("".join(m))

    print(ans_min, ans_max)
