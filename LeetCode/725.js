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
 * @return {ListNode[]}
 */
var splitListToParts = function(head, k) {
    let listLength = 0;
    let currentNode = head;

    while(currentNode){
        listLength++;
        currentNode=currentNode.next;
    }

    const shareNodeCount = parseInt(listLength / k);
    let restNodeCount = listLength % k;

    const nodeCountList = new Array(k).fill(shareNodeCount);

    for(let i=0;i<nodeCountList.length && restNodeCount>0;i++){
        nodeCountList[i]++;
        restNodeCount--;
    }

    const ans = [];

    currentNode = head;

    for(let i=0;i<k;i++){
        ans.push(currentNode);
        let prevNode = currentNode;

        while(nodeCountList[i]>0){
            nodeCountList[i]--;
            prevNode = currentNode;
            currentNode = currentNode?.next;
        }

        if(prevNode!==null) prevNode.next=null;
    }

    return ans;
};
