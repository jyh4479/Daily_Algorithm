/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {boolean[]} hasApple
 * @return {number}
 */
var minTime = function (n, edges, hasApple) {
    let direction = {}, visited = {}
    for (let edge of edges) {
        if (!direction[edge[1]]) direction[edge[1]] = []
        direction[edge[1]].push(edge[0])
        if (!direction[edge[0]]) direction[edge[0]] = []
        direction[edge[0]].push(edge[1])
    }
    return dfs(0, direction, hasApple, visited)
};

let dfs = (node, direction, hasApple, visited) => {
    visited[node] = true

    let res = 0

    for (let ele of direction[node]) {
        if (visited[ele]) continue
        res += dfs(ele, direction, hasApple, visited)
    }

    if ((res > 0 || hasApple[node]) && node != 0) res += 2

    return res
}