/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    const stringDigits = {
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']
    }

    const ans = [];

    const dfs = (index, sel, string) => {
        if(sel===digits.length){
            ans.push(string.join(""));
            return;
        }

        stringDigits[digits[index]].forEach(data=>{
            string.push(data);
            dfs(index+1, sel+1, string);
            string.pop();
        })
    }

    if(digits.length===0) return [];
    dfs(0, 0, []);

    return ans;
};
