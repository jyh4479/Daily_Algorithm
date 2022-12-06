/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var oddEvenList = function (head) {

    if (!head) return head;

    const evenHead = head?.next;

    let oddCurNode = head;
    let evenCurNode = head?.next;

    while (oddCurNode?.next && evenCurNode?.next) {
        oddCurNode.next = evenCurNode.next;
        oddCurNode = oddCurNode?.next;
        evenCurNode.next = oddCurNode?.next;
        evenCurNode = evenCurNode?.next;
    }

    oddCurNode.next = evenHead;

    return head;
};