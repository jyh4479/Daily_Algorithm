// /**
//  * @param {number[][]} roads
//  * @param {number} seats
//  * @return {number}
//  */
// var minimumFuelCost = function(roads, seats) {
//     const graphObject = {};
//     let n = 0;
//     roads.forEach(road=>{
//         if(graphObject[road[0]]===undefined) graphObject[road[0]] = [];
//         if(graphObject[road[1]]===undefined) graphObject[road[1]] = [];
//
//         n = Math.max(n, Number(road[0]), Number(road[1]));
//         graphObject[road[0]].push(road[1]);
//         graphObject[road[1]].push(road[0]);
//     })
//
//     const leaf = [];
//
//     for(let key in graphObject){
//         if(graphObject[key].length===1) leaf.push(Number(key));
//     }
//
//     console.log(n);
//
//
//
//     // if(leaf.length===0) return 0;
//     // else {
//
//     // }
// };

/**
 * @param {number[][]} roads
 * @param {number} seats
 * @return {number}
 */
var minimumFuelCost = function (roads, seats) {
    const adjList = Array.from({length: roads.length + 1}, () => [])
    for (const [from, to] of roads) {
        adjList[from].push(to);
        adjList[to].push(from);
    }
    let ans = 0;
    const dfs = (node, p) => {
        let here = 1;
        for (const ne of adjList[node]) {
            if (ne != p) {
                here += dfs(ne, node);
            }
        }
        if (p !== -1) {
            ans += Math.ceil(here / seats);
        } else {
            return ans;
        }
        return here;
    };
    return dfs(0, -1);
};