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

// var middleNode = function(head) {

//     let curNode = head;
//     let count = 0;

//     while(curNode!==null){
//         count++;
//         curNode = curNode.next;
//     }

//     const middleCount = Math.ceil((count+1) / 2)

//     let ansNode = head;
//     let ansCount = 1;

//     while(ansNode!==null){
//         if(ansCount===middleCount) return ansNode;
//         ansCount++;
//         ansNode = ansNode.next;
//     }
// };

var middleNode = function (head) {

    let curNode = head;
    let count = 0;
    const nodeArray = [];

    while (curNode !== null) {
        count++;
        nodeArray.push(curNode);
        curNode = curNode.next;
    }

    const middleCount = Math.ceil((count + 1) / 2)

    return nodeArray[middleCount - 1];
};