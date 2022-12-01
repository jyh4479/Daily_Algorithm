/**
 * @param {string} s
 * @return {boolean}
 */
var halvesAreAlike = function (s) {
    const vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];

    const a = s.substring(0, s.length / 2);
    const b = s.substring(s.length / 2);

    let countA = 0;
    let countB = 0;

    for (let i = 0; i < a.length; i++) {
        if (vowels.includes(a[i])) countA++;
    }

    for (let i = 0; i < b.length; i++) {
        if (vowels.includes(b[i])) countB++;
    }

    return countA === countB;
};