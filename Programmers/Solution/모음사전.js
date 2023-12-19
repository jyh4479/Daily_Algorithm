function solution(word) {
    const ansObj = {};
    let count = 0;
    const wordList = ['A', 'E', 'I', 'O', 'U'];
    const selectedWordList = [];

    const dfs = (sel) => {

        ansObj[selectedWordList.join('')] = count++;

        if (sel === wordList.length) return;

        for (let i = 0; i < wordList.length; i++) {
            selectedWordList.push(wordList[i]);
            dfs(sel + 1);
            selectedWordList.pop();
        }
    }

    dfs(0);

    return ansObj[word];
}
