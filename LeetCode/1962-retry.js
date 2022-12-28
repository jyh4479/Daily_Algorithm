// /**
//  * @param {number[]} piles
//  * @param {number} k
//  * @return {number}
//  */
// var minStoneSum = function(piles, k) {
//     const ans = piles.map(data=>data);
//     ans.sort((a,b)=>a-b);

//     for(let i=0;i<k;i++){
//         const maxValue = Math.ceil(ans.pop()/2);

//         let mid;
//         let start = 0;
//         let end = ans.length - 1;

//         while(start<=end){

//             mid = parseInt((start+end)/2);

//             if(maxValue<ans[mid]){
//                 end = mid-1
//             }
//             else {
//                 start = mid+1
//             }
//         }
//         ans.splice(end+1, 0, maxValue);
//     }

//     return ans.reduce((a,b)=>a+b,0);
// }

var minStoneSum = function(piles, k) {
    let sum = 0;
    let element;
    let half;
    const pq = new MaxPriorityQueue({ priority: (bid) => bid });

    for (let i = 0; i < piles.length; ++i) {
        sum += piles[i];
        pq.enqueue(piles[i]);
    }

    for (let i = 0; i < k; ++i) {
        element = pq.dequeue().element;
        half = Math.floor(element / 2);
        sum -= half;
        pq.enqueue(element - half);
    }

    return sum;
};