/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */
var minReorder = function(n, edges) {
    function Node(val) {
        this.val = val
        
        this.neighs = new Set()
        this.nexts = new Set()
        this.isDyed = false
        
        Node.map.set(val, this)
    }
    Node.map = new Map()
    Node.get = val => Node.map.get(val)
    
    
    // build nodes
    for (let i = 0; i < n; i++) {
        const node = new Node(i)
    }
    
    // build edges
    for (const edge of edges.values()) {
        const [fromVal, toVal] = edge
        const fromNode = Node.get(fromVal)
        const toNode = Node.get(toVal)
        
        fromNode.neighs.add(toNode)
        toNode.neighs.add(fromNode)
        fromNode.nexts.add(toNode)
    }
    
    
    // start processing
    let result = 0
    function dye(node) {
        node.isDyed = true
        
        for (const neigh of node.neighs.values()) {
            if (neigh.isDyed)   continue
            
            // when the link's direction should have been reversed
            if (node.nexts.has(neigh)) {
                result++
            }
            dye(neigh)
        }
    }
    
    const capital = Node.get(0)
    dye(capital)
    
    
    return result
};
