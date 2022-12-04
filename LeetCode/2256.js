/**
 * @param {number[]} nums
 * @return {number}
 */
//Test case 60 / 78
//Time Limit Exceeded
var minimumAverageDifference = function(nums) {
    let ans=0;
    let minValue = Number.MAX_VALUE;

    for(let i=0;i<nums.length;i++){
        const leftArray = nums.slice(0,i+1);
        const rightArray = nums.slice(i+1);

        const leftSum = Math.floor(leftArray.reduce((a,b)=>a+b,0)/leftArray.length);
        const rightSum = rightArray.length !== 0 ? Math.floor(rightArray.reduce((a,b)=>a+b,0)/rightArray.length) : 0 ;

        const curValue = Math.abs(leftSum-rightSum);
        if(curValue < minValue){
            minValue = curValue;
            ans=i;
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