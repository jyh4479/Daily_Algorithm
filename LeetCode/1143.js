/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function (text1, text2) {
    const ansArray = [];

    for (let i = 0; i < text2.length; i++) {
        ansArray.push(new Array(text1.length).fill(0));
    }

    for (let i = 0; i < text2.length; i++) {
        for (let j = 0; j < text1.length; j++) {
            const subText1 = text1[j];
            const subText2 = text2[i];

            const left = j - 1;
            const up = i - 1;

            if (subText1 === subText2) {
                if (up < 0 || left < 0) ansArray[i][j] = 1;
                else ansArray[i][j] = ansArray[up][left] + 1;
            } else {
                if (up < 0 && left < 0) ansArray[i][j] = 0;
                else if (up < 0) ansArray[i][j] = Math.max(ansArray[i][left], 0);
                else if (left < 0) ansArray[i][j] = Math.max(ansArray[up][j], 0);
                else ansArray[i][j] = Math.max(ansArray[up][j], ansArray[i][left]);
            }
        }
    }

    const result = ansArray[text2.length - 1][text1.length - 1];
    return isNaN(result) ? 0 : result;
};