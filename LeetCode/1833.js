/**
 * @param {number[]} costs
 * @param {number} coins
 * @return {number}
 */
var maxIceCream = function (costs, coins) {
    costs.sort((a, b) => a - b);

    let curCoins = coins;
    let ans = 0;

    for (let i = 0; i < costs.length; i++) {
        if (curCoins < costs[i]) break;
        curCoins -= costs[i];
        ans++;
    }

    return ans;
};
//greedy