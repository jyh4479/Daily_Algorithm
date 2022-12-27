/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function (nums) {
    let ans = false;
    let needStep = 1;

    if (nums.length <= 1) return true;

    for (let i = nums.length - 2; i >= 0; i--) {
        if (nums[i] >= needStep) {
            ans = true;
            needStep = 1;
        } else {
            ans = false;
            needStep += 1;
        }
    }

    return ans;
};
