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
 * @return {TreeNode}
 */
var invertTree = function (root) {

    const dfs = (node) => {
        if (node.left !== undefined && node.left !== null) dfs(node.left);
        if (node.right !== undefined && node.right !== null) dfs(node.right);

        const tmpNode = node.left;
        node.left = node.right;
        node.right = tmpNode;
    }

    if (root !== undefined && root !== null) dfs(root);
    return root;

};