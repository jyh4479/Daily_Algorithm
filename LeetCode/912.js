// /**
//  * @param {number[]} nums
//  * @return {number[]}
//  */
// var sortArray = function(nums) {
//     return nums.sort((a,b)=>Number(a)-Number(b));
// };

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function (nums) {

    const plusList = new Array(5 * (10 ** 4) + 1).fill(0);
    const minusList = new Array(5 * (10 ** 4) + 1).fill(0);

    nums.forEach(data => data < 0 ? minusList[-data] += 1 : plusList[data] += 1);

    const ansList = [];
    for (let i = minusList.length - 1; i > 0; i--) {
        if (minusList[i] !== 0) {
            let count = minusList[i];
            while (count > 0) {
                ansList.push(-i);
                count -= 1;
            }
            ;
        }
    }
    for (let i = 0; i < plusList.length; i++) {
        if (plusList[i] !== 0) {
            let count = plusList[i];
            while (count > 0) {
                ansList.push(i);
                count -= 1;
            }
        }
    }

    return ansList;
};