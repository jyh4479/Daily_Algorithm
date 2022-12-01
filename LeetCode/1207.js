/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function (arr) {
    const resultObject = {};
    const checkObject = {};

    arr.forEach(data => {
        if (resultObject[data] === undefined) {
            resultObject[data] = 1;
        } else {
            resultObject[data]++;
        }
    })


    for (let key in resultObject) {
        if (checkObject[resultObject[key]] === undefined) {
            checkObject[resultObject[key]] = true;
        } else {
            return false;
        }
    }
    return true;
};