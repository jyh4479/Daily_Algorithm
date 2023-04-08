/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {Node} node
 * @return {Node}
 */
var cloneGraph = function(node) {
    const nodeObj = {};
    const linkVisit = [];

    const dfs = (originalNode) => {
        if(originalNode===null) return;

        if(nodeObj[originalNode.val]===undefined) nodeObj[originalNode.val] = new Node(originalNode.val, []);
        originalNode.neighbors.forEach(neighborNode=>{
            if(nodeObj[neighborNode.val]===undefined) {
                dfs(neighborNode);
            }
        });
    }

    const link = (originalNode) => {
        if(originalNode===null) return;

        linkVisit.push(originalNode.val);

        originalNode.neighbors.forEach(neighborNode=>{
            nodeObj[originalNode.val].neighbors.push(nodeObj[neighborNode.val]);
            if(!linkVisit.includes(neighborNode.val)) link(neighborNode);
        });
    }

    dfs(node);  
    link(node);

    const nodeList = [];
    for(let key in nodeObj){
        nodeList.push(nodeObj[key]);
    }

    return nodeList.length > 0 ? nodeList[0] : null;
};
