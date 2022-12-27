var maximumBags = function (capacity, rocks, additionalRocks) {
    let arr = [], res = 0
    for (let q = 0; q < capacity.length; q++) {
        arr[q] = capacity[q] - rocks[q]
    }
    arr.sort((a, b) => a - b)
    for (let q = 0; q < arr.length; q++) {
        additionalRocks -= arr[q]
        if (additionalRocks < 0) return res
        res++
    }
    return res
};