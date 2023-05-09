/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    const ans = [];
    const visited = [];
    const dir=[[0,1],[1,0],[0,-1],[-1,0]];

    for(let i=0;i<matrix.length;i++){
        visited.push(new Array(matrix[0].length).fill(false));
    }

    let direction = 0;
    let cury=0;
    let curx=0;

    while(true){
        if(ans.length===matrix.length*matrix[0].length) break;

        ans.push(matrix[cury][curx]);
        visited[cury][curx]=true;

        const dy = cury + dir[direction][0];
        const dx = curx + dir[direction][1];

        if(dy < 0 || dx < 0 || dy >= matrix.length || dx >= matrix[0].length || visited[dy][dx]){
            direction = (direction + 1) % 4;
            cury = cury + dir[direction][0];
            curx = curx + dir[direction][1];
        } else {
            cury = dy;
            curx = dx;
        }
    }

    return ans;
};
