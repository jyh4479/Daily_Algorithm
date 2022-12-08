/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
const compareArray = (a, b) => {
    if (a.length !== b.length) return false;
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false;
    return true;
}

const leafSimilar = function (root1, root2) {

    const ans1 = [];
    const ans2 = [];

    function move(node, ans) {
        if (node.left === null && node.right === null) {
            ans.push(node.val);
            return;
        } else {
            if (node.left !== null) move(node.left, ans);
            if (node.right !== null) move(node.right, ans);
        }
    }

    move(root1, ans1);
    move(root2, ans2);

    const result = compareArray(ans1, ans2);

    return result;
};