/**
 * @param {number[]} arr
 * @return {number}
 */
var minJumps = function (arr) {

    if (arr.length <= 1) return 0;

    let map = {};
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] in map) {
            map[arr[i]].push(i);
        } else {
            map[arr[i]] = [i];
        }
    }

    let currentLayer = [0];
    let visited = new Set();
    let res = 0;

    while (currentLayer.length > 0) {
        let nextLayer = [];

        for (let idx of currentLayer) {
            if (idx === arr.length - 1) {
                return res;
            }

            //Same value
            for (let same of map[arr[idx]]) {
                if (!visited.has(same)) {
                    visited.add(same);
                    nextLayer.push(same);
                }
            }

            map[arr[idx]] = [];

            //Neighbors
            let left = idx - 1;
            let right = idx + 1;
            if (left >= 0 && !visited.has(left)) {
                visited.add(left);
                nextLayer.push(left);
            }

            if (right < arr.length && !visited.has(right)) {
                visited.add(right);
                nextLayer.push(right);
            }
        }

        currentLayer = nextLayer; //Change array reference
        res++;
    }
};