var longestPalindromeSubseq = function(s) {
    const cache = {};
    const longestPal = (left, right) => {
        const key = `${(left).toString()},${(right).toString()}`;
        if (key in cache) return cache[key]
        
        if (left >= right) return left === right ? 1 : 0;
       
        if (s[left] === s[right]) return 2 + longestPal(left+1, right-1);
        
        cache[key] = Math.max(longestPal(left+1, right), longestPal(left, right-1));
        
        return cache[key]
    }
    return longestPal(0,s.length-1);
};
