/**
 * @param {string[]} strs
 * @return {number}
 */
const checkSorted = (str) => {
    if (str.length === 1) return true;

    let prev = str[0];
    for (let i = 1; i < str.length; i++) {
        if (prev > str[i]) return false;
        prev = str[i];
    }

    return true;
}

var minDeletionSize = function (strs) {
    let ans = 0;
    const columnStrs = [];

    for (let j = 0; j < strs[0].length; j++) {
        let columnStr = "";
        for (let i = 0; i < strs.length; i++) {
            columnStr += strs[i][j];
        }
        columnStrs.push(columnStr);
    }

    columnStrs.forEach(str => {
        checkSorted(str) ? null : ans++;
    })

    return ans;
};