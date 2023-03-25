/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
const getAns = (countList) => {
    let ans = 0;

    for (let i = 0; i < countList.length; i++) {
        for (let j = i + 1; j < countList.length; j++) {
            ans += countList[i] * countList[j];
        }
    }

    return ans;
}

var countPairs = function (n, edges) {
    const componentCountList = [];
    const visited = new Array(n).fill(false);
    const vertexObj = {};

    // build object
    for (let i = 0; i < n; i++) vertexObj[i] = [];

    edges.forEach(edge => {
        vertexObj[edge[0]].push(edge[1]);
        vertexObj[edge[1]].push(edge[0]);
    })

    // check vertex count
    let vertexCount = 0;

    const dfs = (vertex) => {
        if (!visited[vertex]) {
            visited[vertex] = true;
            vertexCount += 1;
            vertexObj[vertex].forEach(nextVertex => dfs(nextVertex));
        } else return;
    }

    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i);
            componentCountList.push(vertexCount);
            vertexCount = 0;
        }
    }


    return componentCountList.length <= 1 ? 0 : getAns(componentCountList);
};
