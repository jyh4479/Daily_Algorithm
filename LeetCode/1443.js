/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {boolean[]} hasApple
 * @return {number}
 */
var minTime = function (n, edges, hasApple) {
    const graph = {};
    const visited = new Array(n).fill(false);

    for (let i = 0; i < n; i++) {
        graph[i] = [];
    }
    edges.forEach(edge => {
        graph[edge[0]].push(edge[1]);
        graph[edge[1]].push(edge[0]);
    })

    const dfs = (vertex) => {
        for (let i = 0; i < graph[vertex].length; i++) {
            if (!visited[graph[vertex][i]]) {
                visited[graph[vertex][i]] = true;
                const childApple = dfs(graph[vertex][i]);
                if (childApple) hasApple[vertex] = childApple;
            }
        }

        if (hasApple[vertex]) return true;
        else return false;
    }

    visited[0] = true;
    hasApple[0] = dfs(0);

    let count = 0;
    hasApple.forEach(apple => apple ? count++ : count);
    return count === 0 ? 0 : (count - 1) * 2;
};
//상현님 아이디어