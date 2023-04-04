/**
 * @param {string} s
 * @return {number}
 */
var partitionString = function(s) {
    const subString = []; 
    let checkSubString = [];

    for(let i=0;i<s.length;i++){
        if(!checkSubString.includes(s[i])) checkSubString.push(s[i]);
        else {
            subString.push(checkSubString.join(""));
            checkSubString = [s[i]];
        }
    }

    if(checkSubString.length>0) subString.push(checkSubString.join(""));
    return subString.length;
};
