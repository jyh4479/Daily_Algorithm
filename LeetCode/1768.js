/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {

    const word1List = word1.split("");
    const word2List = word2.split("");

    const ans = [];
    
    while(word1List.length>0 || word2List.length>0){
        if(word1List.length>0) ans.push(word1List.shift());
        if(word2List.length>0) ans.push(word2List.shift());
    }

    return ans.join("");
};
