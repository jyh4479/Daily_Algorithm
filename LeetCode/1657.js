/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */
var closeStrings = function (word1, word2) {

    const word1Object = {};
    const word2Object = {};

    const q1 = []; // 알파벳 종류 체크 queue
    const q2 = [];

    const q3 = []; // 종류별 개수 체크 queue
    const q4 = [];

    for (let i = 0; i < word1.length; i++) {
        if (word1Object[word1[i]] === undefined) {
            word1Object[word1[i]] = 1;
        } else {
            word1Object[word1[i]]++;
        }
    }

    for (let i = 0; i < word2.length; i++) {
        if (word2Object[word2[i]] === undefined) {
            word2Object[word2[i]] = 1;
        } else {
            word2Object[word2[i]]++;
        }
    }

    for (let key in word1Object) {
        q1.push(key);
        q3.push(word1Object[key]);
    }
    for (let key in word2Object) {
        q2.push(key);
        q4.push(word2Object[key]);
    }

    q1.sort();
    q2.sort();
    q3.sort();
    q4.sort();

    // 1 모든 종류의 알파벳이 존재하는지 확인
    if (!(q1.join("") === q2.join(""))) return false;

    // 2 알파벳 종류별 개수가 같은지 (ex a 2개 ,b 2개 --> 종류별 개수가 같음)
    if (!(q3.join("") === q4.join(""))) return false;


    return true;
};