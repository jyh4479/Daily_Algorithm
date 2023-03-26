/**
 * @param {number[]} edges
 * @return {number}
 */
var longestCycle = function (edges) {
    const vertexObj = {};
    const visited = new Array(edges.length).fill(false);

    let ans = -1;

    const dfs = (startVertex, vertex, edgeCount) => {
        //cycle
        if (edgeCount !== 0 && (startVertex === vertex)) {
            ans = Math.max(ans, edgeCount);
        } else {
            if (!visited[vertex]) {
                visited[vertex] = true;
                dfs(startVertex, edges[vertex], edgeCount + 1);
                visited[vertex] = false;
            }
        }
    }

    edges.forEach((nextVertex, currentVertex) => {
        dfs(currentVertex, currentVertex, 0);
    })

    return ans;
};
