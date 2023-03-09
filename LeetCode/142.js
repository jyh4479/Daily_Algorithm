/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function(head) {
    let curNode = head;

    while(curNode!==null){
        if(curNode.visited===undefined) curNode.visited=true;
        else return curNode;
        curNode=curNode.next;
    }
    return null;
};
