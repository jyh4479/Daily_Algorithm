/**
 * @param {number[]} nums
 * @return {number}
 */
var minimizeArrayValue = function(nums) {
    let sum = 0;
    let maxNum = 0;
    nums.forEach((num, key) => {
        sum += num;
        maxNum = Math.max(maxNum, Math.floor((sum + key) / (key + 1)))
    })
    return maxNum
};
