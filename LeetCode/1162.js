/**
 * @param {number[][]} grid
 * @return {number}
 */
const bfs = (land, grid, n, m) => {
    const {y, x} = land;
    const dir = [[0, 1], [1, 0], [-1, 0], [0, -1]];

    const q = [[y, x]];
    while (q.length >= 1) {
        const curPosition = q.shift();
        for (let i = 0; i < 4; i++) {
            const dy = curPosition[0] + dir[i][0];
            const dx = curPosition[1] + dir[i][1];

            if (dy < 0 || dx < 0 || dy >= n || dx >= m || (grid[dy][dx] !== 0) && (grid[dy][dx] <= grid[curPosition[0]][curPosition[1]] + 1)) continue;

            q.push([dy, dx]);
            grid[dy][dx] = grid[curPosition[0]][curPosition[1]] + 1;
        }
    }
}

var maxDistance = function (grid) {
    const n = grid.length;
    const m = grid[0].length;

    const landList = [];

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (grid[i][j] === 1) landList.push({y: i, x: j});
        }
    }

    landList.forEach(land => {
        bfs(land, grid, n, m);
    })

    let ans;
    grid.forEach(data => {
        ans = ans > Math.max(...data) ? ans : Math.max(...data);
    });
    return ans - 1 < 1 ? -1 : ans - 1;

};
