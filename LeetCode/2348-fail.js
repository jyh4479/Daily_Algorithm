/**
 * @param {number[]} nums
 * @return {number}
 */
var zeroFilledSubarray = function (nums) {
    let ans = 0;

    for (let arrayLength = 1; arrayLength <= nums.length; arrayLength++) {
        let subArrayCount = 0;
        for (let i = 0; i + arrayLength <= nums.length; i++) {
            const subArray = nums.slice(i, i + arrayLength);
            const filteredArray = subArray.filter(data => data !== 0);
            if (filteredArray.length === 0) subArrayCount += 1;
        }
        ans += subArrayCount;
    }

    return ans;
};
