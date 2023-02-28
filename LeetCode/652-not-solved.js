var findDuplicateSubtrees = function (root) {

    const duplicates = new Map();
    const set = new Set();

    const dfs = (node) => {

        // define the basic/leave node key as node as node value
        node.key = node.key || node.val;

        // perform DFS (postorder), and add left and right
        // node keys to the current node key
        if (node.left) {
            dfs(node.left);
            node.key += `-${node.left.key}`;
        } else {
            node.key += 'n'; // null
        }

        if (node.right) {
            dfs(node.right);
            node.key += `-${node.right.key}`;
        } else {
            node.key += 'n'; // null
        }

        // example node keys at this point:
        // ---------------------------------
        // 4nn
        // 2-4nnn
        // 3-2-4nnn-4nn
        // 1-2-4nnn-3-2-4nnn-4nn

        // add duplicated item to the map
        if (set.has(node.key)) {
            duplicates.set(node.key, node);
        } else {
            set.add(node.key);
        }

    };

    dfs(root);

    return Array.from(duplicates.values());
};