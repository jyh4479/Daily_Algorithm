var jump = function (nums) {

    let jumpsRequired = 0, currenJumpEnd = 0, farthest = 0;

    for (let g = 0; g < nums.length - 1; g++) {
        farthest = Math.max(farthest, nums[g] + g);
        if (g == currenJumpEnd) {
            jumpsRequired++;
            currenJumpEnd = farthest;
        }
    }

    return jumpsRequired;
};