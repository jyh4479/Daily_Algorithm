/**
 * @param {number[]} nums
 * @return {number}
 */

// var minimumAverageDifference = function(nums) {
//     let ans=0;
//     let minValue = Number.MAX_VALUE;

//     for(let i=0;i<nums.length;i++){
//         const leftArray = nums.slice(0,i+1);
//         const rightArray = nums.slice(i+1);

//         const leftSum = Math.floor(leftArray.reduce((a,b)=>a+b,0)/leftArray.length);
//         const rightSum = rightArray.length !== 0 ? Math.floor(rightArray.reduce((a,b)=>a+b,0)/rightArray.length) : 0 ;

//         const curValue = Math.abs(leftSum-rightSum);
//         if(curValue < minValue){
//             minValue = curValue;
//             ans=i;
//         }

//     }
//     return ans;
// };

var minimumAverageDifference = function (nums) {
    //memoization으로 reduce 연산 속도 줄이기
    let ans = 0;
    let minValue = Number.MAX_VALUE;

    let leftLength = 0;
    let leftSum = 0;
    let rightLength = nums.length;
    let rightSum = nums.reduce((a, b) => a + b, 0);

    const check = [];

    for (let i = 0; i < nums.length; i++) {
        leftLength++;
        rightLength--;

        rightLength = rightLength === 0 ? 1 : rightLength;

        leftSum += nums[i];
        rightSum -= nums[i];

        const avgLeft = Math.floor(leftSum / leftLength);
        const avgRight = Math.floor(rightSum / rightLength);

        const curResult = Math.abs(avgLeft - avgRight);

        if (minValue > curResult) {
            ans = i;
            minValue = curResult;
        }
    }

    return ans;
};

/*
Math.ceil() : 소수점 올림, 정수 반환
Math.floor() : 소수점 버림, 정수 반환
Math.round() : 소수점 반올림, 정수 반환
Math.abs() : 절대값 반환
Math.max() : 가장 큰 값 반환
Number.MAX_VALUE : JS 가장 큰값
*/