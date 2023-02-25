// /**
//  * @param {number[]} prices
//  * @return {number}
//  */
// var maxProfit = function(prices) {
//     const ans=[];
//     for(let i=0;i<prices.length-1;i++){
//         let maxValue=Number.MIN_VALUE;
//         for(let j=i+1;j<prices.length;j++){
//             maxValue=Math.max(maxValue,prices[j]-prices[i]);
//         }
//         ans.push(maxValue);
//     }
//     return Math.max(...ans) > 0 ? Math.max(...ans) : 0;
// };

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
    //각 날짜에서 뺄수있는 가장 작은값 구하기
    const dayMinValueList = [];
    for (let i = prices.length - 1; i >= 0; i--) {
        if (i === prices.length - 1) dayMinValueList.push(prices[i]);
        else {
            if (prices[i] > dayMinValueList[dayMinValueList.length - 1]) dayMinValueList.push(prices[i]);
            else dayMinValueList.push(dayMinValueList[dayMinValueList.length - 1]);
        }
    }
    dayMinValueList.reverse();
    const result = prices.map((price, index) => dayMinValueList[index] - price);
    return Math.max(...result);
};