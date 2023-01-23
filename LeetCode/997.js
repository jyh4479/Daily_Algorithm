/**
 * @param {number} n
 * @param {number[][]} trust
 * @return {number}
 */
var findJudge = function (n, trust) {
    const trustObj = {};
    let ans = -1;

    for (let person = 1; person <= n; person++) trustObj[person] = [];
    trust.forEach(trustInfo => {
        trustObj[trustInfo[0]].push(trustInfo[1]);
    })

    const canJudge = [];
    for (let key in trustObj) {
        if (trustObj[key].length === 0) canJudge.push(Number(key));
    }

    canJudge.forEach(judge => {
        let flag = true;
        for (let key in trustObj) {
            if (Number(key) !== Number(judge) && !trustObj[key].includes(judge)) flag = false;
        }
        if (flag) ans = judge;
    })

    return ans;
};