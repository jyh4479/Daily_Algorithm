/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    let numberList = String(num).split("");

    while(numberList.length > 1) {
        const number = numberList.reduce((a,b)=>a + Number(b),0);
        numberList = String(number).split("");
    }

    return numberList.length > 0 ? Number(numberList[0]) : 0;
};
