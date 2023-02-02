var isAlienSorted = function (words, order) {
    for (let i = 1; i < words.length; i++) {
        const a = words[i - 1]
        const b = words[i]
        const maxLen = Math.max(a.length, b.length)
        for (let j = 0; j < maxLen; j++) {
            const indexA = order.indexOf(a[j])
            const indexB = order.indexOf(b[j])
            if (indexA > indexB) {
                return false
            } else if (indexA < indexB) {
                j = maxLen
            }
        }
    }
    return true
};