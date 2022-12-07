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
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var rangeSumBST = function (root, low, high) {
    let ans = 0;

    function moveTree(cur) {
        if (cur === null) return; else {
            if (cur.val >= low && cur.val <= high) ans += cur.val;
            moveTree(cur.left);
            moveTree(cur.right);
        }
    }

    moveTree(root);
    return ans;
};