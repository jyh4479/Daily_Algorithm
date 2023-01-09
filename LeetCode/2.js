/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
    const array1 = [];
    const array2 = [];

    let curNode = l1;
    while (curNode !== undefined && curNode !== null) {
        array1.push(curNode.val);
        curNode = curNode.next;
    }

    curNode = l2;
    while (curNode !== undefined && curNode !== null) {
        array2.push(curNode.val);
        curNode = curNode.next;
    }

    const sum = BigInt(array1.reverse().join("")) + BigInt(array2.reverse().join(""));

    const charToNum = num => BigInt(num);

    const sumArray = Array.from(String(sum), charToNum);

    let headNode = null;
    sumArray.forEach(val => {
        const newNode = new ListNode(val, headNode);
        headNode = newNode;
    })

    return headNode;
};