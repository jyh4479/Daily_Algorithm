/**
 * @param {number} n
 * @param {number[][]} roads
 * @return {number}
 */
var minScore = function (n, roads) {
  const pathObj = {};
  const visited = new Array(n + 1).fill(false);
  let ans = Number.MAX_VALUE;

  roads.forEach((pathData) => {
    const start = pathData[0];
    const end = pathData[1];
    const cost = pathData[2];

    if (pathObj[start] === undefined) pathObj[start] = [];
    if (pathObj[end] === undefined) pathObj[end] = [];

    pathObj[start].push([end, cost]);
    pathObj[end].push([start, cost]);
  });

  const q = [1];

  while (q.length > 0) {
    const vertex = q.pop();
    visited[vertex] = true;

    pathObj[vertex].forEach((pathData) => {
      const target = pathData[0];
      const cost = pathData[1];

      ans = Math.min(ans, cost);

      if (!visited[target]) {
        q.push(target);
      }
    });
  }

  return ans;
};
