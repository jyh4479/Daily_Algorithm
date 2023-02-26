var minDistance = function (text1, text2) {
    let m = text1.length
    let n = text2.length
    let c = new Array(m + 1).fill(0)
    c.forEach((x, index) => {
        c[index] = new Array(n + 1)
    })
    let b = []
    for (let j = 0; j <= m; j++)
        c[j][0] = j
    for (let j = 0; j <= n; j++)
        c[0][j] = j

    for (let i = 1; i <= m; i++)
        for (let j = 1; j <= n; j++) {
            var delta = 0
            if (text1[i - 1] != text2[j - 1])
                delta = 1
            c[i][j] = Math.min(c[i - 1][j] + 1, c[i][j - 1] + 1, c[i - 1][j - 1] + delta)
        }

    return c[m][n]
};