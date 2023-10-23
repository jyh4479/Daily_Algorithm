/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
const getAvg = (currentIndex, range, nums) => {
    let sum = 0;
    const cd = 2 * range + 1;

    for (let i = currentIndex - range; i <= currentIndex + range; i++) {
        sum += nums[i];
    }
    return Math.floor(sum / cd);
}

var getAverages = function (nums, k) {
    const centerIndex = k;
    const ans = [];

    if (k === 0) return nums;

    for (let i = 0; i < nums.length; i++) {
        if (i < k || i >= nums.length - k) ans.push(-1);
        else ans.push(getAvg(i, k, nums));
    }

    return ans;
};
