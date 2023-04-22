/**
 * @param {string} s
 * @return {number}
 */
var minInsertions = function(s) {
    let N = s.length;    
    let dp = Array.from({length:N}, ()=>(new Array(N).fill(0)));
    
    for (let l=2; l<=N; l++){
        for (let i=0; i<N; i++){
            let j = i+l-1;
            if (j >= N) break;
            if (s[i] === s[j]){
                dp[i][j] = dp[i+1][j-1];
            }else{
                dp[i][j] = Math.min(dp[i+1][j], dp[i][j-1]) + 1;
            }
            
        }
    }
    return dp[0][N-1];
};
