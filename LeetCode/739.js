/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function (temperatures) {
    const ans = new Array(temperatures.length).fill(0);

    for (let i = 0; i < temperatures.length - 1; i++) {
        let count = 1;
        for (let j = i + 1; j < temperatures.length; j++) {
            if (temperatures[i] < temperatures[j]) {
                ans[i] = count;
                break;
            }
            count++;
        }
    }

    return ans;
};