function solution(n, words) {
    const wordObject = {};
    let prev = "";

    for (let i = 0; i < words.length; i++) {
        if (wordObject[words[i]] === undefined) {

            if (i !== 0 && prev[prev.length - 1] !== words[i][0]) {
                return [(i % n) + 1, parseInt(i / n) + 1];
            }

            wordObject[words[i]] = true;
        } else return [(i % n) + 1, parseInt(i / n) + 1];
        prev = words[i];
    }

    return [0, 0];
}