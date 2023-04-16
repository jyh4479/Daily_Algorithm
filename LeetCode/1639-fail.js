// /**
//  * @param {string[]} words
//  * @param {string} target
//  * @return {number}
//  */
// const ansCheck = (wordList, target) => {
//     let ansCount = 0;

//     const ansCheckDfs = (index, start) => {
//         const word = wordList[index];
//         const checkChar = target[index];

//         if(word===undefined) return;

//         for(let i=start;i<word.length;i++){
//             if(word[i]===checkChar){
//                 if(index===target.length-1) {
//                     ansCount+=1;
//                     continue;
//                 }
//                 ansCheckDfs(index+1,i+1);
//             }
//         }
//     }

//     ansCheckDfs(0,0);

//     return ansCount;
// }

// var numWays = function(words, target) {
//   const wordsLength = words.length;
//   const wordsVisited = new Array(words.length).fill(false);
//   const wordList = [];

//   let ans = 0;

//   const wordDfs = () => {
//       if(wordList.length===wordsLength){
//           ans += ansCheck(wordList, target);
//           return;
//       }

//       for(let i=0;i<words.length;i++){
//           if(!wordsVisited[i]){
//                wordsVisited[i]=true;
//                wordList.push(words[i]);
//                wordDfs();
//                wordList.pop();
//                wordsVisited[i]=false;
//           }
//       }
//   }

//   wordDfs();

//   return ans;
// };

/**
 * @param {string[]} words
 * @param {string} target
 * @return {number}
 */
var numWays = function(words, target) {
     const mod = 1e9 + 7, res = new Array(target.length + 1).fill(0);
    res[0] = 1;
    for (let i = 0; i < words[0].length; i++) {
        let count = new Array(26).fill(0);
        for (let word of words) {
            count[word.charCodeAt(i) - 97]++;
        }
        for (let j = target.length - 1; j >= 0; --j) {
            res[j + 1] += res[j] * count[target.charCodeAt(j) - 97] % mod;
        }
    }
    return res[target.length] % mod;
};
