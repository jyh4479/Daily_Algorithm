/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
class SortedList {
    nodeHead = null;
    nodeCount = 0;

    addNodeList = (node) => {
        if (this.nodeCount === 0) {
            this.nodeCount += 1;
            this.nodeHead = node;
            return;
        }

        if (node.val <= this.nodeHead.val) {
            this.nodeCount += 1;
            node.next = this.nodeHead;
            this.nodeHead = node;
            return;
        }

        let prevNode = this.nodeHead;
        let curNode = this.nodeHead;
        while (curNode !== null) {
            curNode = curNode.next;

            if (curNode === null) {
                prevNode.next = node;
                return;
            }

            if (node.val < curNode.val) {
                prevNode.next = node;
                node.next = curNode;
                return;
            }

            prevNode = prevNode.next;
        }
    }

    getNodeList = () => {
        return this.nodeHead;
    }
};

var mergeKLists = function (lists) {
    const nodeValueList = [];
    const sortedList = new SortedList();

    lists.forEach(listHead => {
        let curNode = listHead;
        while (curNode !== null) {
            const check = new ListNode(curNode.val, null);
            sortedList.addNodeList(check);
            curNode = curNode.next;
        }
    })

    return sortedList.getNodeList();
};