/**
 * @param {number[]} nums
 * @return {number}
 */
// var zeroFilledSubarray = function(nums) {
//     let ans = 0;

//     for(let arrayLength=1;arrayLength<=nums.length;arrayLength++){
//         let subArrayCount = 0;
//         for(let i=0;i+arrayLength<=nums.length;i++){
//             const subArray = nums.slice(i,i+arrayLength);
//             const filteredArray = subArray.filter(data=>data!==0);
//             if(filteredArray.length===0) subArrayCount+=1;
//         }
//         ans+=subArrayCount;
//     }

//     return ans;
// };

var zeroFilledSubarray = function (nums) {
    const zeroObj = {};

    let zeroCount = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 0) zeroCount += 1;
        else {
            if (zeroCount === 0) continue;
            if (zeroObj[zeroCount] === undefined) {
                zeroObj[zeroCount] = 1;
            } else {
                zeroObj[zeroCount] += 1;
            }
            zeroCount = 0;
        }
    }

    if (zeroCount !== 0) {
        if (zeroObj[zeroCount] === undefined) {
            zeroObj[zeroCount] = 1;
        } else {
            zeroObj[zeroCount] += 1;
        }
    }

    let ans = 0;
    for (let key in zeroObj) {
        while (zeroObj[key] > 0) {
            const num = Number(key);
            zeroObj[key] -= 1;
            ans += ((num * (num + 1)) / 2);
        }
    }
    return ans;
};

// 1 - 1
// 2 - 3
// 3 - 6
// 4 - 10
// 5 - 15
// 6 - 21
