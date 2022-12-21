// /**
//  * @param {number} n
//  * @param {number[][]} dislikes
//  * @return {boolean}
//  */
// const groupCheck = (currentGroup, myDisLike) =>{
//     for(let i=0;i<myDisLike.length;i++){
//         const data=myDisLike[i];
//         if(currentGroup.includes(data)) {
//             return false;
//         }
//     }
//     return true;
// }

// var possibleBipartition = function(n, dislikes) {
//     const group1 = [];
//     const group2 = [];
//     const likeList = {};

//     for(let i=1;i<=n;i++){
//         likeList[i]=[];
//     }

//     dislikes.forEach(data=>{
//         likeList[data[0]].push(data[1]);
//         likeList[data[1]].push(data[0]);
//     })

//     group1.push(1);
//     for(let i=2;i<=n;i++){
//         if(groupCheck(group1, likeList[i])){
//             group1.push(i);
//             continue;
//         }
//         if(groupCheck(group2, likeList[i])){
//             group2.push(i);
//             continue;
//         }
//         return false;
//     }
//     return true;
// };

var g1 = {};
var g2 = {};
var doneKey = {};

var possibleBipartition = function (N, d) {
    var h = {};
    g1 = {};
    g2 = {};
    doneKey = {};

    for (var i = 0; i < d.length; i++) {
        var p1 = d[i][0];
        var p2 = d[i][1];
        if (h[p1]) {
            h[p1].push(p2);
        } else {
            h[p1] = [p2];
        }
        if (h[p2]) {
            h[p2].push(p1);
        } else {
            h[p2] = [p1];
        }
    }

    for (var key in h) {
        if (!doneKey[key]) {
            if (nextGroup(key, h) === false) return false;
        }
    }

    return true;
};

var nextGroup = function (key, h) {
    var keyInLeft = !!g1[key];
    var keyInRight = !!g2[key];
    doneKey[key] = true;
    if (!h[key]) return;
    if (keyInLeft || (!keyInLeft && !keyInRight)) {
        for (var i = 0; i < h[key].length; i++) {
            var v = h[key][i];
            if (g1[v]) {
                return false;
            }
            g2[v] = true;
        }
    } else if (keyInRight) {
        for (var i = 0; i < h[key].length; i++) {
            var v = h[key][i];
            if (g2[v]) {
                return false;
            }
            g1[v] = true;
        }
    }

    for (var i = 0; i < h[key].length; i++) {
        if (doneKey[h[key][i]]) continue;
        if (nextGroup(h[key][i], h) === false) return false;
    }
}