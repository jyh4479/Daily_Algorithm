
const maxPoints = points => {
    const n = points.length
    if (n === 1) return 1

    let res = 2
    for (let i = 0; i < n; i++) {
        const cnt = {}
        for (let j = 0; j < n; j++) {
            if (j === i) continue
            key = Math.atan2(points[j][1] - points[i][1],
                points[j][0] - points[i][0])
            cnt[key] = (cnt[key] || 1) + 1
        }
        res = Math.max(res, ...Object.values(cnt))
    }

    return res
}