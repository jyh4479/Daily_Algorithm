/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function (s) {
    //조건
    //1. 반복횟수 내림차순으로 정렬
    const stringObj = {};

    for (let i = 0; i < s.length; i++) {
        stringObj[s[i]] === undefined ? stringObj[s[i]] = 1 : stringObj[s[i]]++;
    }

    const stringArray = [];

    for (let key in stringObj) {
        stringArray.push([key, stringObj[key]]);
    }

    stringArray.sort((a, b) => {
        return b[1] - a[1];
    });

    ans = [];

    stringArray.forEach(data => {
        for (let i = 0; i < data[1]; i++) {
            ans.push(data[0]);
        }
    });

    return ans.join("");
};

//Object.entries + reduce 등 다양한 js 함수로 코드 축소가능