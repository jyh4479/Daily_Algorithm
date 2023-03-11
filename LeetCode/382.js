/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 */
var Solution = function(head) {
    this.listHead = head;
};

/**
 * @return {number}
 */
Solution.prototype.getRandom = function() {
    const nodeValueList = [];
    let curNode = this.listHead;

    while(curNode!==null){
        nodeValueList.push(curNode.val);
        curNode = curNode.next;
    }
    
    const min = Math.ceil(0);
    const max = Math.floor(nodeValueList.length);

    return nodeValueList[Math.floor(Math.random() * (max - min)) + min];
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(head)
 * var param_1 = obj.getRandom()
 */
