/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function (nums, n) {
    const listA = nums.slice(0, n);
    const listB = nums.slice(n, nums.length);

    const result = [];
    for (let i = 0; i < listA.length; i++) {
        result.push(listA[i]);
        result.push(listB[i]);
    }

    return result;
};