/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    const size = nums.length;
    const visited = new Array(size).fill(false);

    const currentSelected = [];
    const ans = [];

    const dfs = (sel) => {

        if(sel===size){
            ans.push(currentSelected.slice());
            return;
        }

        for(let i=0;i<size;i++){
            if(!visited[i]){
                visited[i]=true;
                currentSelected.push(nums[i]);
                dfs(sel+1);
                visited[i]=false;
                currentSelected.pop(nums[i]);
            }
        }
    }

    dfs(0);

    return ans;
};
