/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {

    for (let i = 2; i < nums.length; i++) {
        if (i - 3 < 0) nums[i] = nums[i] + nums[i - 2];
        else nums[i] = Math.max(nums[i] + nums[i - 2], nums[i] + nums[i - 3]);
    }

    return Math.max(...nums);
};