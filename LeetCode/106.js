var buildTree = function (inorder, postorder) {
    let postorder_idx = postorder.length - 1;

    // create easy inorder mapping for referrence 
    let inorderMapping = new Map();
    for (let i = 0; i < inorder.length; i++) {
        inorderMapping.set(inorder[i], i);
    }

    // postorder idx determines the root 
    let createTree = (in_left, in_right) => {
        // handle the empty tree
        if (in_left > in_right || postorder_idx < 0) return null;
        let key = postorder[postorder_idx];
        let root = new TreeNode(key);

        // find pivot
        let pivot = inorderMapping.get(key);

        // decrement the post order idx before checking children 
        postorder_idx--;

        // split right because we are handling
        // post order (left -> right -> process)
        // Here we proccess the node, traverse right, then left
        root.right = createTree(pivot + 1, in_right);

        // split left 
        root.left = createTree(in_left, pivot - 1);

        // return the root
        return root;
    }

    return createTree(0, inorder.length - 1);
};
