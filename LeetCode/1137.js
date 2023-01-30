/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function (n) {
    const memo = new Array(38).fill(0);
    memo[0] = 0;
    memo[1] = 1;
    memo[2] = 1;

    for (let i = 3; i < memo.length; i++) memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3];

    return memo[n];
};
