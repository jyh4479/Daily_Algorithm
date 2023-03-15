// /**
//  * @param {number[]} piles
//  * @param {number} h
//  * @return {number}
//  */
// var minEatingSpeed = function(piles, h) {

//     const resultList = [];

//     let left = 1;
//     let right = Math.max(...piles);

//     let mid = parseInt((left + right) / 2);
//     let minResult = Number.MAX_VALUE;

//      while(left<=right) {
//         let checkPiles = piles.map(pile=>pile);
//         let currentHour = 0;

//         for(let i=0;i<checkPiles.length;i++){
//             while(checkPiles[i] > 0) {
//                 currentHour+=1;
//                 checkPiles[i]-=mid;
//             }
//         }

//         if(h >= currentHour){
//             //더 적은 수로 먹어봐야함
//             minResult = Math.min(minResult, mid);
//             right=mid-1;
//             mid=parseInt((left + right) / 2);
//         } else {
//             //더 많은 수로 먹어야함
//             left=mid+1;
//             mid=parseInt((left + right) / 2);
//         }
//      }

//      return minResult;
// };

let a, h;
const minEatingSpeed = (piles, H) => {
    a = piles, h = H;
    return BinarySearch(0, Number.MAX_SAFE_INTEGER)
};

const BinarySearch = (low, high) => {
    while (low <= high) {
        let mid = low + parseInt((high - low) / 2);
        if (possible(mid)) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return low;
};

const possible = (k) => {
    let needHour = 0;
    for (const x of a) needHour += Math.ceil(x / k);
    return needHour > h;
};
