var WordDictionary = function () {
    this.wordList = [];
};

/**
 * @param {string} word
 * @return {void}
 */
WordDictionary.prototype.addWord = function (word) {
    this.wordList.push(word);
};

/**
 * @param {string} word
 * @return {boolean}
 */
WordDictionary.prototype.search = function (word) {
    if (word.includes('.')) {
        let matchingWord = this.wordList.filter(data => data.length === word.length);
        for (let i = 0; i < word.length; i++) {
            if (word[i] !== '.') {
                matchingWord = matchingWord.filter(data => data[i] === word[i]);
            } else continue;
        }
        return matchingWord.length > 0 ? true : false;
    } else {
        if (this.wordList.includes(word)) return true;
        else return false;
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
