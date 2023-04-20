var widthOfBinaryTree = function(root) {
    let depth = 0
    let rowArray = [[]]
    rowArray[0].push(BigInt(1))
    callChildren(BigInt(1),1,rowArray,root)

    console.log(rowArray)
    let max = BigInt(0)
    for (var row of rowArray) {
        rowmax = BigInt(1) + row[row.length-1] - row[0]
  //      console.log('rowmax is ' + rowmax)
        max = (max < rowmax) ? rowmax : max
    }
    return max
};

function callChildren(parent, depth, rowArray,node) {
    if (rowArray[depth] == null && (node.left !=null || node.right !=null)) {rowArray[depth] = []}
    if (node.left !=null) {
        rowArray[depth].push(BigInt(2)*parent)
        callChildren(BigInt(2)*parent,depth+1,rowArray,node.left)
    }
    if (node.right !=null) {
        rowArray[depth].push((BigInt(2)*parent)+BigInt(1)) 
        callChildren((BigInt(2)*parent)+BigInt(1), depth+1,rowArray,node.right)
    }
}
