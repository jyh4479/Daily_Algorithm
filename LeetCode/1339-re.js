// /**
//  * Definition for a binary tree node.
//  * function TreeNode(val, left, right) {
//  *     this.val = (val===undefined ? 0 : val)
//  *     this.left = (left===undefined ? null : left)
//  *     this.right = (right===undefined ? null : right)
//  * }
//  */
// /**
//  * @param {TreeNode} root
//  * @return {number}
//  */
// const getTreeSum = (root) => {
//     let sum = 0;
//     const stack = [root];
//
//     while (stack.length !== 0) {
//         const node = stack.pop();
//         sum += node.val;
//
//         if (node.left !== null) stack.push(node.left);
//         if (node.right !== null) stack.push(node.right);
//     }
//
//     return sum;
// }
//
// const maxProduct = function (root) {
//
//     let ans = -Infinity;
//     const allNodeSum = getTreeSum(root);
//     const stack = [root];
//
//     while (stack.length !== 0) {
//         const node = stack.pop();
//         if (node.left !== null) {
//             const subTreeSum = getTreeSum(node.left);
//             ans = Math.max(ans, subTreeSum * (allNodeSum - subTreeSum));
//         }
//         if (node.right !== null) {
//             const subTreeSum = getTreeSum(node.right);
//             ans = Math.max(ans, subTreeSum * (allNodeSum - subTreeSum));
//         }
//
//         if (node.left !== null) stack.push(node.left);
//         if (node.right !== null) stack.push(node.right);
//     }
//
//     return ans % 1000000007;
// };

var maxProduct = function (root) {
    let max = 0;

    const sum = (node, o) => {
        if (!node) return;
        o.total += node.val;

        sum(node.left, o);
        sum(node.right, o);
    };

    let to = {total: 0};

    sum(root, to);


    let tt = to.total;


    const fn = (node, mysum) => {
        if (!node) return;

        let me = node.val;
        let lefttotal = 0, righttotal = 0

        if (!node.left) {
            lefttotal = 0;
            righttotal = mysum - me;
        } else if (!node.right) {
            righttotal = 0;
            lefttotal = mysum - me;
        } else {
            let lo = {total: 0};
            sum(node.left, lo);
            lefttotal = lo.total;
            righttotal = mysum - me - lefttotal;
        }


        if (node.left && lefttotal * (tt - lefttotal) > max) {
            max = lefttotal * (tt - lefttotal);
        }

        if (node.right && righttotal * (tt - righttotal) > max) {
            max = righttotal * (tt - righttotal);
        }

        fn(node.left, lefttotal);
        fn(node.right, righttotal);
    };

    fn(root, tt, true);

    return max % (10 ** 9 + 7);
};