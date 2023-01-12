// /**
//  * @param {number} n
//  * @param {number[][]} edges
//  * @param {string} labels
//  * @return {number[]}
//  */
// var countSubTrees = function(n, edges, labels) {
//     const graph = {};
//     const visited = new Array(n).fill(false);
//     const vertexString = new Array(n).fill("");

//     for(let i=0;i<n;i++){
//         vertexString[i]+=labels[i];
//         graph[i]=[];
//     }

//     edges.forEach(edge=>{
//         graph[edge[0]].push(edge[1]);
//         graph[edge[1]].push(edge[0]);
//     })

//     const dfs = (vertex) => {
//         for(let i=0;i<graph[vertex].length;i++){
//             if(!visited[graph[vertex][i]]){
//                 visited[graph[vertex][i]]=true;
//                 vertexString[vertex]+=dfs(graph[vertex][i]);
//             }
//         }
//         return vertexString[vertex];
//     }

//     visited[0]=true;
//     vertexString[0]=dfs(0);

//     const ans = [];
//     for(let i=0;i<n;i++){
//         ans.push(vertexString[i].split(labels[i]).length-1);
//     }
//     return ans;
// };

var countSubTrees = function (n, edges, labels) {

    const h = {}
    for (let i = 0; i < edges.length; i++) {
        const [a, b] = edges[i]
        if (a in h) h[a].push(b)
        else h[a] = [b]
        if (b in h) h[b].push(a)
        else h[b] = [a]
    }


    const ans = new Array(n).fill(0)
    const trace = new Set()
    const counters = new Array(26).fill(0)

    const walk = (node = 0) => {
        trace.add(node)

        const idx = labels[node].charCodeAt(0) - 97
        const was = counters[idx]
        counters[idx]++

        const eds = h[node]
        for (let i = 0; i < eds.length; i++) {
            const next = eds[i]
            if (!trace.has(next)) {
                walk(next)
            }
        }
        ans[node] = counters[idx] - was

        return ans
    }

    return walk()
};