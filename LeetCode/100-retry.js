// /**
//  * Definition for a binary tree node.
//  * function TreeNode(val, left, right) {
//  *     this.val = (val===undefined ? 0 : val)
//  *     this.left = (left===undefined ? null : left)
//  *     this.right = (right===undefined ? null : right)
//  * }
//  */
// /**
//  * @param {TreeNode} p
//  * @param {TreeNode} q
//  * @return {boolean}
//  */
// let ans = true;

// var isSameTree = function(p, q) {
//     if((p?.val!==q?.val) || (p===null&&q!==null) || (p!==null&&q===null)) ans = false;

//     if(p!==null && q!==null){
//         isSameTree(p.left, q.left);
//         isSameTree(p.right, q.right);
//     }

//     return ans;
// };

var isSameTree = function (p, q) {
    if (!p && !q) {
        return true;
    }
    if (!p || !q || p.val !== q.val) {
        return false;
    }
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};