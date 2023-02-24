// /**
//  * @param {number[]} weights
//  * @param {number} days
//  * @return {number}
//  */
// const getNeedDays = (weights, capacity) => {
//     let result = 1;
//     let curSum = 0;
//     let min = Number.MAX_VALUE;

//     if(weights.length===0) return [0, 0];

//     for(let i=0;i<weights.length;i++){
//         if((curSum + weights[i]) <= capacity) curSum+=weights[i];
//         else {
//             console.log(capacity)
//             console.log(curSum)
//             min = Math.min(min, curSum);
//             result+=1;
//             curSum=0;
//         }
//     }

//     return [result, min];
// }
 
// var shipWithinDays = function(weights, days) {
//     let capacity = weights.reduce((a,b)=>a+b,0);
//     let needDays = 0;
//     let ans = 0;

//     while(needDays<days){
//         [needDays, ans] = getNeedDays(weights, capacity);
//         capacity-=1;
//     }

//     return ans;
// };

const sm = (a) => a.reduce(((x, y) => x + y), 0);

let a, d;
const shipWithinDays = (weights, days) => {
    a = weights, d = days;
    let sum = sm(a);
    if (d == 1) return sum;
    if (sum % d == 0 && new Set(a).size == 1) return sum / d;
    return BinarySearch(Math.max(...a), Number.MAX_SAFE_INTEGER); // min value should be at least max, otherwise it cannot take max anyway
};

const BinarySearch = (low, high) => {
    while (low <= high) {
        let mid = low + parseInt((high - low) / 2);
        if (possible(mid)) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return low;
};

const possible = (cap) => {
    let needDays = 1, sum = 0;
    for (const x of a) {
        if (sum + x > cap) {
            sum = x;
            needDays++;
        } else if (sum + x == cap) {
            sum = 0;
            needDays++;
        } else {
            sum += x;
        }
    }
    return needDays > d;
};
