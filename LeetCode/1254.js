/**
 * @param {number[][]} grid
 * @return {number}
 */
var closedIsland = function(grid) {
    const dir = [[-1,0],[0,1],[1,0],[0,-1]];
    const islands = [];
    let check = true;
    let ans = 0;

    grid.map(row => islands.push(row));
 
    const dfs = (y, x) => {

        islands[y][x]=1;
        if(y >= grid.length-1 || x >= grid[0].length-1 || y <= 0 || x <= 0) check=false;

        for(let i=0;i<4;i++){
            const dy=y+dir[i][0];
            const dx=x+dir[i][1];

            if(dy >= grid.length || dx >= grid[0].length || dy < 0 || dx < 0 || islands[dy][dx]===1) continue;
            if(dy >= grid.length-1 || dx >= grid[0].length-1 || dy <= 0 || dx <= 0) check=false;

            islands[dy][dx]=1;
            dfs(dy, dx);
        }
    }

    for(let i=0;i<islands.length;i++){
        for(let j=0;j<islands[0].length;j++){
            if(islands[i][j]===0) {
                dfs(i,j);
                if(check) ans+=1;
                check=true;
            }
        }
    }
    
    return ans;
};
