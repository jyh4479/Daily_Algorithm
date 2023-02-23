/**
 * @param {number} k
 * @param {number} w
 * @param {number[]} profits
 * @param {number[]} capital
 * @return {number}
 */
var findMaximizedCapital = function (k, w, profits, capital) {
    let capitalsQueue = new MinPriorityQueue();
    let profitsQueue = new MaxPriorityQueue();
    for (let i = 0; i < capital.length; i++)
        capitalsQueue.enqueue([capital[i], profits[i]], capital[i]);

    for (let i = 0; i < k; i++) {
        while (!capitalsQueue.isEmpty() && capitalsQueue.front().element[0] <= w) {
            let el = capitalsQueue.dequeue().element;
            profitsQueue.enqueue(el, el[1]);
        }
        if (profitsQueue.isEmpty()) return w;
        w += profitsQueue.dequeue().element[1];
    }
    return w;
};
