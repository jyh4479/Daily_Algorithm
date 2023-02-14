// /**
//  * @param {string} a
//  * @param {string} b
//  * @return {string}
//  */
// var addBinary = function(a, b) {

//     let aValue = 0;
//     let bValue = 0;

//     for(let i=a.length-1;i>=0;i--){
//         if(a[a.length-1-i]==='1') aValue+=2**i;
//     }
//     for(let i=b.length-1;i>=0;i--){
//         if(b[b.length-1-i]==='1') bValue+=2**i;
//     }

//     let sum = BigInt(aValue + bValue);
//     if(sum===0n) return '0';

//     console.log(sum)

//     const ans = [];
//     while(sum>0){
//         ans.push(sum % 2n);
//         sum=sum / 2n;
//     }

//     return ans.reverse().join("");
// };

/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */

var addBinary = function (a, b) {
    let ai = a.length - 1
    let bi = b.length - 1
    let rem = 0
    let result = ""

    while (ai >= 0 || bi >= 0) {
        let av = ai >= 0 ? parseInt(a[ai]) : 0
        let bv = bi >= 0 ? parseInt(b[bi]) : 0

        let sum = av ^ bv ^ rem
        rem = (av & bv) || (av ^ bv && rem ? 1 : 0)
        result = sum + result

        ai--
        bi--
    }

    return rem == 1 ? rem + result : result
};