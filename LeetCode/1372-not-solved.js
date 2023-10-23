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
var longestZigZag = function (root) {
  const ans = { val: 0 };
  dfs(root, ans);

  return ans.val;
};

function dfs(root, ans) {
  if (!root) return [-1, -1];

  const [_, rightVal] = dfs(root.left, ans);
  const [leftVal, __] = dfs(root.right, ans);

  const takeLeft = 1 + rightVal;
  const takeRight = 1 + leftVal;
  ans.val = Math.max(ans.val, takeLeft, takeRight);

  return [takeLeft, takeRight];
}
