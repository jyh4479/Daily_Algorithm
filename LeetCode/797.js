/**
 * @param {number[][]} graph
 * @return {number[][]}
 */
var allPathsSourceTarget = function (graph) {
    const SIZE = graph.length;

    const ans = [0];
    const ansList = [];

    const dfs = (node, target) => {
        if (node === target) {
            ansList.push(ans.slice());
        } else {
            graph[node].forEach(nextNode => {
                ans.push(nextNode);
                dfs(nextNode, target);
                ans.pop();
            });
        }
    }

    dfs(0, SIZE - 1);

    return ansList;
};