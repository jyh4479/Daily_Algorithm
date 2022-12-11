var maxPathSum = function(root) {
    let maxPathSumNum = -Infinity;

    const maxPathSumRec = function(node){
        if(!node){
            return 0;
        }

        let leftMax = Math.max(maxPathSumRec(node.left), 0);
        let rightMax = Math.max(maxPathSumRec(node.right), 0);
        maxPathSumNum = Math.max(maxPathSumNum, leftMax + rightMax + node.val);
        return Math.max(leftMax, rightMax) + node.val;
    };

    maxPathSumRec(root);
    return maxPathSumNum;
};