/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    //left, down, right
    const dir = [[0,1],[1,0]];
    const m = grid.length;
    const n = grid.length===0 ? 0 : grid[0].length;
    const visited = [];
    const memo = [];
    for(let i=0;i<m;i++) visited.push(new Array(n).fill(false));
    for(let i=0;i<m;i++) memo.push(new Array(n).fill(Number.MAX_VALUE));

    const dfs = (y, x, cost) => {

        for(let i=0;i<dir.length;i++){
            const dy = y + dir[i][1];
            const dx = x + dir[i][0];

            if(dy < 0 || dx < 0 || dy >= m || dx >= n || visited[dy][dx] || memo[dy][dx] <= cost + grid[dy][dx]) continue;

            visited[dy][dx]=true;
            memo[dy][dx]=cost + grid[dy][dx];
            dfs(dy, dx, memo[dy][dx]);
            visited[dy][dx]=false;
        }
    }

    visited[0][0]=true;
    memo[0][0]=grid[0][0];
    dfs(0,0,memo[0][0]);


    return memo[m-1][n-1];
};
