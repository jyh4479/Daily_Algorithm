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
 * @return {boolean}
 */
var isSymmetric = function(root) {
    const leftList = [];
    const rightList =[];

    const preOrder = (node) => {
        if(node===null) {
            leftList.push(null);
            return;
        } else {
            leftList.push(node.val);
            preOrder(node.left);
            preOrder(node.right);
        }
    }

    const postOrder = (node) => {
        if(node===null) {
            rightList.push(null);
            return;
        } else {
            rightList.push(node.val);
            postOrder(node.right);
            postOrder(node.left);
        }
    }

    preOrder(root.left);
    postOrder(root.right);

    if(leftList.length!==rightList.length) return false;
    for(let i=0;i<leftList.length;i++){
        if(leftList[i]!==rightList[i]) return false;
    }
    return true;
};

// var isSymmetric = function(root) {
//   if(!root) return true;
//   return dfs(root.left, root.right);
// };

// function dfs(s, t){
//   if(!s && !t) return true;
//   if(!s || !t) return false;
//   if(s.val !== t.val) return false;
  
//   return dfs(s.left, t.right) && dfs(s.right, t.left)
// }
