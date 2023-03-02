// /**
//  * @param {character[]} chars
//  * @return {number}
//  */
// var compress = function(chars) {
//     chars.sort();
//     const ansObj = {};
//     const ans = [];

//     chars.forEach(char=>{
//         if(ansObj[char]===undefined) ansObj[char]=0;
//         ansObj[char]+=1;
//     })

//     while(chars.length>0) chars.pop();

//     for(let key in ansObj){
//         if(ansObj[key]===1) chars.push(key);
//         else chars.push(key, ...String(ansObj[key]).split(""));
//     }

//     return chars.length;
// };

/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function (chars) {
    let l = 0, r = 0;
    let ind = 0;
    while (l < chars.length) {
        r = l;
        while (r < chars.length && chars[r] == chars[l])
            r++;

        let nxt = r--;

        chars[ind++] = chars[l];
        if (l != r)
            for (let ch of (1 + r - l).toString())
                chars[ind++] = ch;
        l = nxt;
    }

    return ind;
};