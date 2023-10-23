/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if(x < 0) return false;
    const stringNumber = String(x).split("").reverse().join("");
    const reversedNumber = Number(stringNumber);

    return x === reversedNumber;
};
