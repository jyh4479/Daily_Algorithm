/**
 * // Definition for a QuadTree node.
 * function Node(val,isLeaf,topLeft,topRight,bottomLeft,bottomRight) {
 *    this.val = val;
 *    this.isLeaf = isLeaf;
 *    this.topLeft = topLeft;
 *    this.topRight = topRight;
 *    this.bottomLeft = bottomLeft;
 *    this.bottomRight = bottomRight;
 * };
 */

/**
 * @param {number[][]} grid
 * @return {Node}
 */
var construct = function (grid) {
    let n = grid.length;

    /**
     * Takes uppers left coordinate of grid, and length of the grid to calculate whether
     * the grid has the same value.
     *
     * @param {number[]} start - upper left coordinates of the quadrant to check.
     * @param {number} size - size of the quadrant to check.
     *
     * @returns {number} If all values are the same return that value. If values are different return -1.
     */
    const checkValue = (start, size) => {
        let valToCheck = grid[start[0]][start[1]];
        let [row, col] = start;
        for (let i = row; i < row + size; i++) {
            for (let j = col; j < col + size; j++) {
                if (valToCheck !== grid[i][j]) {
                    return -1;
                }
            }
        }

        return valToCheck;
    };

    /**
     * Recursive function to create the the quad-tree.
     *
     * @param {number[]} start - upper left coordinate of grid.
     * @param {number} size - size of the grid.
     *
     * @returns {Node} root of the Quad-Tree.
     */
    const createNode = (start, size) => {
        let value = checkValue(start, size);

        // If all values are the same, or if the size of the grid is 1, return as a leaf node.
        if (value !== -1 || size === 1) {
            let n = new Node(value, true, null, null, null, null);
            return n;
        }

        // New size of the grid is half of the current size.
        let nextSize = size / 2;

        // Calculate new upper left coordinates for each quadrant
        let [row, col] = start;

        let topLeft = createNode(start, nextSize);
        let topRight = createNode([row, col + nextSize], nextSize);
        let bottomLeft = createNode([row + nextSize, col], nextSize);
        let bottomRight = createNode([row + nextSize, col + nextSize], nextSize);

        return new Node(1, false, topLeft, topRight, bottomLeft, bottomRight);
    };

    return createNode([0, 0], n);

};