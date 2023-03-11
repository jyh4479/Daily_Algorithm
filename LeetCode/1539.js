/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var findKthPositive = function(arr, k) {
    const missingIntegers = new Array(2001).fill(true);
    const result = [];

    arr.forEach(integer=>missingIntegers[integer]=false);
    missingIntegers.forEach((integer, index)=>{
        if(missingIntegers[index]) result.push(index);
    })

    return result[k];
};
