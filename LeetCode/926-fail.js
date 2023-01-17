// /**
//  * @param {string} s
//  * @return {number}
//  */
// var minFlipsMonoIncr = function(s) {
//     let count_zero = 0;
//     let count_one = 0;

//     let check_first_one = false;
//     for(let i=0;i<s.length;i++){
//         if(s[i]==='1') check_first_one = true;
//         if(check_first_one) {
//             if(s[i]==='0') count_zero++;
//             else if(s[i]==='1') count_one++;
//         }
//     }
//     for(let i=s.length-1;i>0;i--){
//         if(s[i]!=='1') break;
//         count_one--;
//     }


//     if(s.length===count_one) return 0;
//     if(count_zero<count_one) return count_zero;
//     if(count_zero>count_one) return count_one;
//     return count_one;
// };

var minFlipsMonoIncr = function (s) {
    const n = s.length;
    let zeros = 0;

    for (let i = n - 1; i >= 0; i--) {
        if (s.charAt(i) === "0") zeros++;
    }

    let minFlips = Number.MAX_SAFE_INTEGER;
    let ones = 0;

    for (let i = 0; i < n; i++) {
        const digit = s.charAt(i);

        minFlips = Math.min(minFlips, ones + zeros);

        if (digit === "1") ones++;
        else zeros--;
    }

    minFlips = Math.min(minFlips, ones + zeros);

    return minFlips;
};