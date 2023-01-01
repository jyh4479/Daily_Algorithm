/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
Object.prototype.checkIncludes = function (words) {
    for (let key in this) {
        if (this[key] === words) return true;
    }
    return false;
}

var wordPattern = function (pattern, s) {
    const patterns = pattern.split('');
    const words = s.split(' ');
    const wordObject = {};

    if (patterns.length !== words.length) return false;

    for (let i = 0; i < patterns.length; i++) {
        const curPattern = patterns[i];
        const curWord = words[i];

        if (wordObject[curPattern] === undefined) {
            if (!wordObject.checkIncludes(curWord)) wordObject[curPattern] = curWord;
            else return false;
        } else {
            if (wordObject[curPattern] === curWord) continue;
            else return false;
        }
    }

    return true;
};