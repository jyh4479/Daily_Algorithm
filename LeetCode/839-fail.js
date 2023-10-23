/**
 * @param {string[]} A
 * @return {number}
 */
/** MY WORKING VERSION **/
var numSimilarGroups = function(A) {
    const al = {};
    let groups = new Set();
    let seen = new Set();
 
    const isSimilar = (word1, word2) => {
        let diff = 0, i = 0;
        while(i < word1.length) {
            if (word1[i] !== word2[i]) {
               diff += 1; 
            }
            i++;
            continue;
        }
        return diff <= 2;
    }
    
    /** Create AL (Directed Graph)  of similar words **/
    for (let i = 0; i < A.length; i++) {
        al[A[i]] = [];
		/*
		 * We want edge from A[i] to A[j] and also A[j] to A[i],
		 * there for we start the loop j = 0 instead of j = i+1
		*/
        for (let j = 0; j < A.length; j++) {
            if(i === j) continue;
            if (isSimilar(A[i], A[j])) {
                al[A[i]].push(A[j]);
            } 
        }
    }

    /* Do DFS om the adjacency list */
    const dfs = (grp, str) => {
        seen.add(str);
        if(al[str] === undefined) return;
        groups.add(grp);
        for(let swap of al[str]) {
            if(!seen.has(swap)) dfs(grp, swap);
        }

    }    
    for(let str of A) {
        if(!seen.has(str)) dfs(str, str);
    }
    return groups.size;
};
