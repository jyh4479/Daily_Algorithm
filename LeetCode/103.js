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
 * @return {number[][]}
 */
var zigzagLevelOrder = function (root) {

    const resultObj = {};

    const dfs = (node, level) => {
        if (node.left !== null && node.left !== undefined) dfs(node.left, level + 1);
        if (node.right !== null && node.right !== undefined) dfs(node.right, level + 1);

        if (resultObj[level] === undefined) resultObj[level] = [];
        resultObj[level].push(node.val);
    }

    if (root !== null && root !== undefined) dfs(root, 0);

    const result = [];
    for (let key in resultObj) {
        if (Number(key) % 2 === 1) resultObj[key].reverse();
        result.push(resultObj[key]);
    }
    
    return result;
};