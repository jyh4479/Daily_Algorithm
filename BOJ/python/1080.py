def changeMaps(i, j):
    global maps
    for a in range(i, i + 3):
        for b in range(j, j + 3):
            if maps[a][b] == 1:
                maps[a][b] = 0
            else:
                maps[a][b] += 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    global maps
    maps, checkmaps = [], []
    ans = 0

    for i in range(n):
        maps.append(list(map(int, input())))
    for i in range(n):
        checkmaps.append(list(map(int, input())))

    if n >= 3 and m >= 3:
        for i in range(n - 2):
            for j in range(m - 2):
                if maps[i][j] != checkmaps[i][j]:
                    ans += 1
                    changeMaps(i, j)

    for i in range(n):
        if maps[i] != checkmaps[i]:
            ans = -1

    print(ans)
