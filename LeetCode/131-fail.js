/**
 * @param {string} s
 * @return {string[][]}
 */
const isPalindrome = (palindromeString) => {
    if (palindromeString.length === 1) return true;
    if (palindromeString === palindromeString.split("").reverse().join("")) return true;
    return false;
}

const isEqualArray = (a, b) => {
    if (a.length !== b.length) return false;
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false;
    return true;
}

var partition = function (s) {
    const ans = [];

    for (let sel = 1; sel <= s.length; sel++) {
        const subAns = [];
        let curIndex = 0;

        while (curIndex < s.length) {
            //sel 값에 대비해 가장 큰 부분부터 확인
            for (let selCount = sel; selCount >= 1; selCount--) {
                if (isPalindrome(s.slice(curIndex, curIndex + selCount))) {
                    subAns.push(s.slice(curIndex, curIndex + selCount));
                    curIndex = curIndex + selCount;
                    break;
                }
            }
        }

        let pushFlag = true;
        for (let i = 0; i < ans.length; i++) {
            if (isEqualArray(ans[i], subAns)) {
                pushFlag = false;
                continue;
            }
        }
        if (pushFlag) ans.push(subAns);
    }

    return ans;
};