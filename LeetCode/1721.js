/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var swapNodes = function(head, k) {
    let listLength = 0;

    let curNode = head;
    while(curNode!==null){
        listLength++;
        curNode=curNode.next;
    }

    let curCount = 0;
    let firstNode;
    let secondNode;
    curNode = head;
    while(curNode!==null){
        curCount++;
        if(curCount===k){
            firstNode=curNode;
        }
        if(curCount===listLength-(k-1)){
            secondNode=curNode;
        }
        curNode=curNode.next;
    }

    [firstNode.val, secondNode.val] = [secondNode.val, firstNode.val];

    return head;
};
