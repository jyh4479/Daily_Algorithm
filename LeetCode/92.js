/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
var reverseBetween = function (head, left, right) {
  const listValueStack = [];

  let currentIndex = 1;
  let currentNode = head;

  while (currentNode) {
    if (currentIndex >= left && currentIndex <= right) {
      listValueStack.push(currentNode.val);
    }

    currentIndex++;
    currentNode = currentNode.next;
  }

  currentIndex = 1;
  currentNode = head;
  let ansHead = null;
  let currentAnsNode = null;

  while (currentNode) {
    if (currentIndex === left) {
      while (listValueStack.length > 0) {
        const value = listValueStack.pop();
        const newNode = new ListNode(value, null);

        if (ansHead === null) {
          ansHead = newNode;
          currentAnsNode = ansHead;
        } else {
          currentAnsNode.next = newNode;
          currentAnsNode = currentAnsNode.next;
        }

        currentIndex++;
        currentNode = currentNode.next;
      }
    } else {
      const value = currentNode.val;
      const newNode = new ListNode(value, null);

      if (ansHead === null) {
        ansHead = newNode;
        currentAnsNode = ansHead;
      } else {
        currentAnsNode.next = newNode;
        currentAnsNode = currentAnsNode.next;
      }

      currentIndex++;
      currentNode = currentNode.next;
    }
  }

  return ansHead;
};
