/**
 * @param {string[]} pizza
 * @param {number} k
 * @return {number}
 */
var ways = function(pizza, k) {
    var matrix=[],cache={},ans;
    //Create a 2D array from the given array of strings 
    for(let i=0;i<pizza.length;i++){
        for(let j=0;j<pizza[i].length;j++){
            if(matrix[i]===undefined){
                matrix[i]=[];
            }
            matrix[i][j]=pizza[i][j];
        }
    }
    /*
    Approach:
    We will search row by row, as soon as we find the first "A", we use every horizontal cut after that row, because the upper part will have atleas one apple
    We will search column by column, as soon as we find the first "A", we use every vertical cut after that column, because the left part will have atleas one apple
    */
    ans = backtrack(0,0,0);
    return ans%1000000007;
    function backtrack(startRow,startCol,cutCount){
        let cacheKey = startRow+"_"+startCol+"_"+cutCount;
        if(cache[cacheKey]!==undefined){
            return cache[cacheKey];
        }
        let hasAppleFlag = hasApple(startRow,startCol);
        if(hasAppleFlag===false){//If this matrix/sub matrix is not having any apple then there is no need to look for anything else.
            return 0;
        }
        if(cutCount===k-1){//If this is the final piece(sub matrix) and its having apple then its an answer 
            return 1;
        }
        let sum=0,found=false;
        //Search row by row, as soon as we find the first "A", we use every horizontal cut after that row, because the upper part will have atleas one apple
        for(let i=startRow;i<matrix.length;i++){
            for(let j=startCol;j<matrix[i].length;j++){
                if(matrix[i][j]==="A"){
                    found=true;
                    //make every horizontal cut after the row iCut
                    for(let iCut=i+1;iCut<matrix.length;iCut++){
                        sum+=backtrack(iCut,startCol,cutCount+1);
                    }
                    break;
                }
            }
            if(found===true){
                break;
            }
        }
        found=false;
        //Search column by column, as soon as we find the first "A", we use every vertical cut after that column, because the left part will have atleas one apple
        for(let j=startCol;j<matrix[0].length;j++){
            for(let i=startRow;i<matrix.length;i++){
                if(matrix[i][j]==="A"){
                    found=true;
                    //Make every vertical cut after the column jCut
                    for(let jCut=j+1;jCut<matrix[i].length;jCut++){
                        sum+=backtrack(startRow,jCut,cutCount+1);
                    }
                    break;
                }
            }
            if(found===true){
                break;
            }
        }
        cache[cacheKey] = sum;
        return cache[cacheKey];
    }
    function hasApple(startRow,startCol){
        for(let i=startRow;i<matrix.length;i++){
            for(let j=startCol;j<matrix[i].length;j++){
                if(matrix[i][j]==="A"){
                    return true;
                }
            }
        }
        return false;
    }
};
