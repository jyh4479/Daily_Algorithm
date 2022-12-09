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
const maxAncestorDiff = function (root) {
    let ans = -Infinity;

    function move(node) {
        if (node === null) return;
        else {
            const curValue = node.val;
            const stack = [];

            if (node.left !== null) stack.push(node.left);
            if (node.right !== null) stack.push(node.right);

            while (stack.length > 0) {
                const checkNode = stack.pop();
                ans = Math.max(Math.abs(curValue - checkNode.val), ans);
                if (checkNode.left !== null) stack.push(checkNode.left);
                if (checkNode.right !== null) stack.push(checkNode.right);
            }
            move(node.left);
            move(node.right);
        }
    }

    move(root);
    return ans;
}