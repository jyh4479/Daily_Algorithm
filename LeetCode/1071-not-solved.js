// /**
//  * @param {string} str1
//  * @param {string} str2
//  * @return {string}
//  */
// var gcdOfStrings = function(str1, str2) {
//     let gcd = "";
//     const bigString = str1.length >= str2.length ? str1 : str2;
//     const smallString = str1.length < str2.length ? str1 : str2;

//     let i=0;
//     let j=smallString.length;

//     while(j<=bigString.length){

//         if(smallString === bigString.slice(i,j)){
//             gcd = smallString;
//             break;
//         }

//         i++;
//         j++;
//     }

//     for(let i=1;i<=gcd.length;i++){
//         //스플릿해서 비교하기
//     }

//     return gcd;
// };

/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function (str1, str2) {
    const [smallerString, largerString] = [str1, str2].sort((a, b) => a.length - b.length);
    for (let i = smallerString.length; i > 0; i--) {
        const testString = smallerString.slice(0, i);
        const correctSmaller = !smallerString.split(testString).join('').length;
        const correctLarger = !largerString.split(testString).join('').length;
        if (correctSmaller && correctLarger) return testString;
    }
    return '';
};