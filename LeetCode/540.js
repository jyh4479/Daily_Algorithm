/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNonDuplicate = function (nums) {
    let prev = 0;
    let current = 1;

    if (nums.length === 1) return nums[0];

    while (current < nums.length) {
        if (nums[prev] !== nums[current]) return nums[prev];
        prev += 2;
        current += 2;
    }
    return nums[prev];
};
