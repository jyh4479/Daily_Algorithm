/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    const stringLength = needle.length;
    
    for(let i=0;i<haystack.length;i++){
        const checkString = haystack.slice(i,i+stringLength);
        if(checkString===needle) return i;
    }
    return -1;
};
