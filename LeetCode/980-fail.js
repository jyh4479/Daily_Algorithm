// /**
//  * @param {number[][]} grid
//  * @return {number}
//  */
// var uniquePathsIII = function(grid) {

//     const endX = grid[0].length;
//     const endY = grid.length;
//     const visited = [];

//     let startPosition;
//     let targetPosition;
//     let targetPathCount = 0;

//     let ans = 0;

//     const dir = [[-1,0],[0,1],[1,0],[0,-1]];

//     for(let i=0;i<grid.length;i++){
//         const visit = [];
//         for(let j=0;j<grid[0].length;j++){

//             visit.push(false);

//             if(grid[i][j]===1){
//                 startPosition = [i,j];
//                 targetPathCount++;
//             } else if(grid[i][j]===2){
//                 targetPosition = [i,j];
//             } else if(grid[i][j]===0){
//                 targetPathCount++;
//             }
//         }
//         visited.push(visit);
//     }

//     const dfs = (curPosition, pathCount) => {
//         const y = curPosition[0];
//         const x = curPosition[1];

//         if(pathCount+1 === targetPathCount && y === targetPosition[0] && x === targetPosition[1]){
//             ans++;
//             return;
//         }

//         if(y < 0 || x < 0 || y >= endY || x >= endX || visited[y][x] || grid[y][x]===-1) return;
//         else {
//             visited[y][x]=true;
//             for(let i=0;i<4;i++){
//                 dfs([y+dir[i][0],x+dir[i][1]],pathCount+1);
//             }
//             visited[y][x]=false;
//         }
//     }

//     dfs(startPosition, 0);

//     return ans;
// };

function uniquePathsIII(grid) {
    if (grid == null || grid.length === 0) return 0;

    const h = grid.length;
    const w = grid[0].length;
    const dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]];
    let start;
    let end;
    let emptyCount = 1;
    let res = 0;

    for (let i = 0; i < h; i++) {
        for (let j = 0; j < w; j++) {
            if (grid[i][j] === 0) emptyCount++;
            else if (grid[i][j] === 1) start = [i, j];
            else if (grid[i][j] === 2) end = [i, j];
        }
    }

    function go(x, y, count) {
        if (grid[x][y] === -1 || grid[x][y] === Infinity) return;

        if (x === end[0] && y === end[1]) {
            if (count === emptyCount) res++;
            return;
        }

        grid[x][y] = Infinity; // Mark visited
        for (const [di, dj] of dirs) {
            const i = x + di;
            const j = y + dj;
            if (i < 0 || i >= h || j < 0 || j >= w) continue;
            go(i, j, count + 1);
        }
        grid[x][y] = 0; // Reset
    }

    go(start[0], start[1], 0);
    return res;
}