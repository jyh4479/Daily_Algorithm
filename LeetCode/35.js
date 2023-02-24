/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function (nums, target) {
    let i = 0;
    while (nums[i] < target) i += 1;
    return i;
};
