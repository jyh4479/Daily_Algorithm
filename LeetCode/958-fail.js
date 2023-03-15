var isCompleteTree = function(root) {
  const q = [root];
  let hasNonNode = false;
  while(q.length) {
    const currNode = q.shift();
    if(currNode === null) {
      hasNonNode = true;
    } else {
      if(hasNonNode) return false;
      q.push(currNode.left)
      q.push(currNode.right);
    }
  }
  return true;
};
