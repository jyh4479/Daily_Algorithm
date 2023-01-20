var findSubsequences = function (nums) {
    if (nums.length < 2) return [];
    var result = [];
    var path = [];
    var backtrack = function (startIndex) {
        if (path.length >= 2) {
            result.push([...path]);
        }
        var used = new Set(); // Important, we need to check whether the num has been used on this level to avoid duplicate
        for (var i = startIndex; i < nums.length; i++) {
            if (path.length > 0 && nums[i] < path[path.length - 1] || used.has(nums[i])) continue;
            used.add(nums[i]);
            path.push(nums[i]);
            backtrack(i + 1);
            path.pop();
        }
        return;
    }
    backtrack(0);
    return result;
};