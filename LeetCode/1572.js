/**
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function(mat) {
    let ans = 0;

    let start = 0;
    let end = mat[0].length-1;
    

    mat.forEach(numberList=>{
        if(start===end) ans+=(numberList[start]);
        else ans+=(numberList[start] + numberList[end]);
        start++;
        end--;
    })

    return ans;
};
