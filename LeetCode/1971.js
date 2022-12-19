/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} source
 * @param {number} destination
 * @return {boolean}
 */
var validPath = function (n, edges, source, destination) {
    const visited = Array(n).fill(false);
    const newEdges = {};
    visited.forEach((d, i) => newEdges[i] = []);

    edges.forEach(data => {
        const start = data[0];
        const end = data[1];

        newEdges[start].push(end);
        newEdges[end].push(start);
    })

    const s = [source];
    while (s.length > 0) {
        const edge = s.pop();
        visited[edge] = true;

        if (edge === destination) return true;

        newEdges[edge].forEach(data => {
            if (!visited[data]) {
                visited[data] = true;
                s.push(data);
            }
        })
    }

    return false;
};