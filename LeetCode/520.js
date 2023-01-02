/**
 * @param {string} word
 * @return {boolean}
 */
const checkCapital = (word) => {
    for (let i = 1; i < word.length; i++) {
        if (word.charCodeAt(i) >= 65 && word.charCodeAt(i) <= 90) return false;
    }
    return true;
}

const checkNoneCapital = (word) => {
    for (let i = 1; i < word.length; i++) {
        if (word.charCodeAt(i) >= 97 && word.charCodeAt(i) <= 122) return false;
    }
    return true;
}

var detectCapitalUse = function (word) {

    if (word.length === 1) return true;

    // 1.첫 글자가 대문자인 경우
    if (word.charCodeAt(0) >= 65 && word.charCodeAt(0) <= 90) {
        // 1-1. 나머지가 모두 소문자
        // 1-2. 나머지가 모두 대문자
        if (!checkCapital(word) && !checkNoneCapital(word)) return false;

    } else {
        // 2.첫 글자가 대문자가 아닌 경우
        // 2-1. 나머지가 모두 소문자
        for (let i = 1; i < word.length; i++) {
            if (word.charCodeAt(i) >= 65 && word.charCodeAt(i) <= 90) return false;
        }
    }

    return true;
};