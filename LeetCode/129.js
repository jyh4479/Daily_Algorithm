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
var sumNumbers = function (root) {
    const numberList = [];
    const currentNumber = [];
    const dfs = (node, number) => {
        currentNumber.push(node.val);

        if (node.left === null && node.right === null) {
            numberList.push(Number(currentNumber.join("")));
            return;
        }
        if (node.left !== null) {
            dfs(node.left, currentNumber);
            currentNumber.pop();
        }
        if (node.right !== null) {
            dfs(node.right, currentNumber);
            currentNumber.pop();
        }
    }
    dfs(root, currentNumber);

    return numberList.reduce((a, b) => a + b, 0);
};
