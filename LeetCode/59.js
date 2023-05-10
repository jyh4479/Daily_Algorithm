/**
 * @param {number} n
 * @return {number[][]}
 */
var generateMatrix = function(n) {
    const ans = [];
    const dir=[[0,1],[1,0],[0,-1],[-1,0]];

    for(let i=0;i<n;i++)ans.push(new Array(n).fill(0));

    let direction = 0;
    let cury=0;
    let curx=0;
    let curNumber=1;

    while(true){
        if(curNumber>n*n) break;

        ans[cury][curx]=curNumber;
        curNumber++;

        const dy = cury + dir[direction][0];
        const dx = curx + dir[direction][1];

        if(dy < 0 || dx < 0 || dy >= n || dx >= n || ans[dy][dx]!==0){
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
