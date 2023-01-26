/**
 * @param {number} n
 * @param {number[][]} flights
 * @param {number} src
 * @param {number} dst
 * @param {number} k
 * @return {number}
 */
var findCheapestPrice = function(n, flights, src, dst, k) {
    const costMatrix = []
    for (let i = 0; i < n; i++) {
        costMatrix.push(new Array(n))
    }

    costMatrix.forEach(r => {
        r[src] = 0
    })

    flights.forEach(f => {
        if (f[0] === src) costMatrix[0][f[1]] = f[2]
    })

    let i = 1
    while (i <= k) {
        const j = i - 1
        flights.forEach(f => {
            const [s,d,c] = f
            if (costMatrix[j][s] !== undefined && costMatrix[j][s] !== Infinity ) {
                if (costMatrix[i][d] === undefined || costMatrix[j][s] + c < costMatrix[i][d]) {
                    costMatrix[i][d] = costMatrix[j][s] + c
                }
            }
        })

        i++
    }

    return costMatrix[k][dst] === undefined || costMatrix[k][dst] === Infinity ? -1 : costMatrix[k][dst]
};