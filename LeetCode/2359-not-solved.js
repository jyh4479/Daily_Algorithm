const closestMeetingNode = (edges, node1, node2) => {
    const n = edges.length;
    const dfs = (i, dist) => {
        const seen = new Set();
        let len = 0;
        while (i != -1) {
            dist[i] = len++;
            seen.add(i);
            if (seen.has(edges[i])) break;
            i = edges[i];
        }
    }
    const n1Dist = Array(n).fill(-1);
    const n2Dist = Array(n).fill(-1);
    dfs(node1, n1Dist);
    dfs(node2, n2Dist);
    let maxim = Number.MAX_SAFE_INTEGER;
    let ans = -1;
    for (let i = 0; i < n; ++i) {
        if (n1Dist[i] == -1 || n2Dist[i] == -1) continue;
        if (Math.max(n1Dist[i], n2Dist[i]) < maxim) {
            ans = i;
            maxim = Math.max(n1Dist[i], n2Dist[i]);
        }
    }
    return ans;
};