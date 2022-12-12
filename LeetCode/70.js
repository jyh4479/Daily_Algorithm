/**
 * @param {number}
 * @return {number}
 */
var climbStairs = function (n) {

    const ansList = new Array(46).fill(0);
    ansList[1] = 1;
    ansList[2] = 2;

    for (let i = 3; i < ansList.length; i++) {
        const prevprevIndex = i - 2;
        const prevIndex = i - 1;
        ansList[i] = ansList[prevprevIndex] + ansList[prevIndex];
    }

    return ansList[n];
};