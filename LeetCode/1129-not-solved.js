/**
 * @param {number} n
 * @param {number[][]} red_edges
 * @param {number[][]} blue_edges
 * @return {number[]}
 */
const shortestAlternatingPaths = (n, redEdges, blueEdges) => {
    const red = 0;
    const blue = 1;
    const graph = Array(n).fill(0).map(n => [[], []]);
    redEdges.forEach(([u, v]) => graph[u][red].push(v));
    blueEdges.forEach(([u, v]) => graph[u][blue].push(v));
    const d = Array(n).fill(0).map(n => [Infinity, Infinity]);
    d[0][red] = 0;
    d[0][blue] = 0;
    let q = [[0, red], [0, blue]];
    while (q.length > 0) {
        const nextQ = [];
        q.forEach(([u, color]) => {
            const out = graph[u][color];
            out.forEach(v => {
                const nextColor = 1 - color;
                const nextDist = d[u][color] + 1;
                if (d[v][nextColor] === Infinity) nextQ.push([v, nextColor]);
                if (d[v][nextColor] > nextDist) d[v][nextColor] = nextDist;
            });
        });
        q = nextQ;
    }
    return graph.map((n, i) => {
        const min = Math.min(d[i][red], d[i][blue]);
        return min === Infinity ? -1 : min;
    });
};