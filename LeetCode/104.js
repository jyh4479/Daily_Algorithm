/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function (root) {
    let ans = 0;

    const dfs = (node, depth) => {
        ans = Math.max(depth, ans);
        if (node?.left !== null && node?.left !== undefined) dfs(node.left, depth + 1);
        if (node?.right !== null && node?.right !== undefined) dfs(node.right, depth + 1);
    }
    if (root !== null && root !== undefined) dfs(root, 1);
    return ans;
};