/**
 * @param {number[]} num
 * @param {number} k
 * @return {number[]}
 */
var addToArrayForm = function (num, k) {
    const sum = String((BigInt(num.join(""))) + BigInt(k)).split("");
    return sum.map(data => Number(data));
};