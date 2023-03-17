var Trie = function() {
    this.wordList = [];
};

/** 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    this.wordList.push(word);
};

/** 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    if(this.wordList.includes(word)) return true;
    else return false;
};

/** 
 * @param {string} prefix
 * @return {boolean}
 */
 //Trie의 startWith
Trie.prototype.startsWith = function(prefix) {
     for(let i = 0 ; i < this.wordList.length ; i++){
         //JS string의 startsWith (다른 함수임)
        if(this.wordList[i].startsWith(prefix)) return true
    }
    return false
};
/** 
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
