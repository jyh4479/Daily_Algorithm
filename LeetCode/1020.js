/**
 * @param {number[][]} grid
 * @return {number}
 */
var numEnclaves = function(grid) {
    const m = grid.length + 2;
    const n = grid[0].length + 2;
    const dir = [[-1,0],[0,1],[1,0],[0,-1]];
    const land = [];

    land.push(new Array(n).fill(2));
    grid.map(data=>land.push([2, ...data, 2]));
    land.push(new Array(n).fill(2));

    const dfs = (y, x) => {
        for(let i=0;i<4;i++){
            const dy=y+dir[i][0];
            const dx=x+dir[i][1];

            if(dy>=m || dx>=n || dy<0 || dx<0 || land[dy][dx]===0 || land[dy][dx]===2) continue;

            land[dy][dx]=2;
            dfs(dy,dx);
        }
    }

    for(let i=0;i<m;i++){
        for(let j=0;j<n;j++){
            if(land[i][j]===2) {
                land[i][j]=2;
                dfs(i,j);
            }
        }
    }

    let ans = 0;
    land.forEach(data=>{
        data.forEach(cell=>{
            if(cell===1) ans++;
        })
    })

    return ans;
};
