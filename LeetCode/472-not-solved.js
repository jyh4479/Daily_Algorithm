/**
 * @param {string[]} words
 * @return {string[]}
 */
var findAllConcatenatedWordsInADict = function (words) {
    const set = new Set(words);
    const rec = (idx, map, s, count) => {
        if (idx === s.length) {
            if (count > 0) {
                return {present: true, count: count};
            }
        }
        if (map.has(idx)) {
            return map.get(idx);
        }
        for (let j = idx + 1; j <= s.length; j++) {
            if (set.has(s.slice(idx, j))) {
                const res = rec(j, map, s, count + 1);
                if (res.present) {
                    map.set(idx, {present: true, count: res.count});
                    return map.get(idx);
                }
            }
        }
        map.set(idx, {present: false, count: count});
        return map.get(idx);
    };
    const result = [];
    for (let i = 0; i < words.length; i++) {
        const map = new Map();
        const res = rec(0, map, words[i], 0);
        if (res.present && res.count > 1) {
            result.push(words[i]);
        }
    }
    return result;
};
