/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function (matrix, target) {
    let y = 0;
    let ans = false;

    for (let i = 0; i < matrix.length; i++) {
        if (i < matrix.length - 1) {
            if (matrix[i][0] <= target && matrix[i + 1][0] > target) {
                console.log(y)
                y = i;
                break;
            }
        } else {
            y = matrix.length - 1;
        }
    }


    for (let j = 0; j < matrix[y].length; j++) {
        if (matrix[y][j] === target) ans = true;
    }

    return ans;
};
