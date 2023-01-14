// /**
//  * @param {string} s1
//  * @param {string} s2
//  * @param {string} baseStr
//  * @return {string}
//  */
// var smallestEquivalentString = function(s1, s2, baseStr) {
//     const stringObj = {};
//     for(let i=0;i<s1.length;i++){
//         stringObj[s1[i]]=[];
//         stringObj[s2[i]]=[];
//     }

//     for(let i=0;i<s1.length;i++){
//         if(!stringObj[s1[i]].includes(s1[i])) stringObj[s1[i]].push(s1[i]);
//         if(!stringObj[s2[i]].includes(s2[i])) stringObj[s2[i]].push(s2[i]);

//         if(!stringObj[s1[i]].includes(s2[i])) stringObj[s1[i]].push(s2[i]);
//         if(!stringObj[s2[i]].includes(s1[i])) stringObj[s2[i]].push(s1[i]);
//     }

//     for(let key in stringObj){
//         for(let i=0;i<stringObj[key].length;i++){
//             const equalKey = stringObj[key][i];
//             for(let j=0;j<stringObj[key].length;j++){
//                 if(!stringObj[equalKey].includes(stringObj[key][j])) stringObj[equalKey].push(stringObj[key][j]);
//             }
//         }
//     }

//     for(let key in stringObj){
//         stringObj[key].sort();
//     }

//     console.log(stringObj)
//     let ans = "";
//     for(let i=0;i<baseStr.length;i++){
//         for(let key in stringObj[baseStr[i]]){
//             if(Number(key)===0){
//                 console.log(baseStr[i],stringObj[baseStr[i]],stringObj[baseStr[i]][key])
//                 ans+=stringObj[baseStr[i]][key];
//             }
//         }
//     }

//     return ans;
// };

const smallestEquivalentString = (s1, s2, baseStr) => {
    const link = {};
    const find = (a) => {
        if (link[a] == null) link[a] = a;
        while (link[a] != a) {
            link[a] = link[link[a]];
            a = link[a];
        }
        return a;
    }
    const union = (a, b) => {
        a = find(a);
        b = find(b);
        if (a > b) {
            let temp = b;
            b = a;
            a = temp;
        }
        link[b] = a;
    }
    for (let i = 0; i < s1.length; i++) {
        union(s1[i], s2[i]);
    }

    let ans = "";
    for (const a of baseStr) {
        ans += find(a);
    }
    return ans;
};