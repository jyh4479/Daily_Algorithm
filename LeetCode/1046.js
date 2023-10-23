/**
 * @param {number[]} stones
 * @return {number}
 */

//TODO:heap으로 구현하면 더 좋을것 같음
var lastStoneWeight = function(stones) {
    let sortedStones = stones.sort((a,b)=>Number(a)-Number(b));

    while(sortedStones.length > 1){
        const firstStone = sortedStones.pop();
        const secondStone = sortedStones.pop();

        firstStone !== secondStone ? sortedStones.push(firstStone - secondStone) : null;

        sortedStones=sortedStones.sort((a,b)=>Number(a)-Number(b));
    }

    return sortedStones.length > 0 ? sortedStones[0] : 0;
};
