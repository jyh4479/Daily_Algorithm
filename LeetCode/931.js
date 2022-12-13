/**
 * @param {number[][]} matrix
 * @return {number}
 */
var minFallingPathSum = function (matrix) {
    const n = matrix.length;
    const ansArray = [];

    for (let i = 0; i < n; i++) {
        ansArray.push(Array(n).fill(Infinity));
    }
    for (let i = 0; i < n; i++) {
        ansArray[0][i] = matrix[0][i];
    }

    for (let i = 1; i < n; i++) {
        for (let j = 0; j < n; j++) {
            const row = i - 1;
            const col = [j - 1, j, j + 1];
            for (let k = 0; k < 3; k++) {
                if (col[k] < 0 || col[k] >= n) continue;
                ansArray[i][j] = Math.min(ansArray[row][col[k]] + matrix[i][j], ansArray[i][j])
            }
        }
    }

    return Math.min(...ansArray[n - 1]);
};