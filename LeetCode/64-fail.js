// /**
//  * @param {number[][]} grid
//  * @return {number}
//  */
// var minPathSum = function(grid) {
//     //left, down, right
//     const dir = [[-1,0],[0,1],[1,0]];
//     const m = grid.length;
//     const n = grid.length===0 ? 0 : grid[0].length;
//     const visited = [];
//     for(let i=0;i<m;i++) visited.push(new Array(n).fill(false));
//     let ans = Number.MAX_VALUE;

//     const dfs = (y, x, cost) => {

//         if(y===(m-1) && x===(n-1)) {
//             ans = Math.min(ans, cost);
//             return;
//         }

//         for(let i=0;i<dir.length;i++){
//             const dy = y + dir[i][1];
//             const dx = x + dir[i][0];

//             if(dy < 0 || dx < 0 || dy >= m || dx >= n || visited[dy][dx]) continue;

//             visited[dy][dx]=true;
//             dfs(dy, dx, cost + grid[dy][dx]);
//             visited[dy][dx]=false;
//         }
//     }

//     visited[0][0]=true;
//     dfs(0,0,grid[0][0]);

//     return ans;
// };

var minPathSum = function(grid) {
    function gett (x,y) {
        if (x<0 || y<0 ) return Infinity
        return grid[x][y]
    }
    grid.forEach((col,x)=>{
        col.forEach((e,y)=>{
            if (x==0 && y==0) return
            grid[x][y] += Math.min(gett(x-1,y),gett(x,y-1))
        })
    })
    return grid[grid.length-1][grid[0].length-1]
};
