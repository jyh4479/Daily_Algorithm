/**
 * @param {number[][]} piles
 * @param {number} k
 * @return {number}
 */
var maxValueOfCoins = function(piles, k) {
    var n = piles.length;
    var cache = {};
    var getMaxValue = function(i, k) {
        if (i >= n || k <= 0) return 0;
        var key = i + ',' + k;
        if (cache[key]) return cache[key];
        var result = getMaxValue(i + 1, k);
        var sum = 0;
        for (var j = 0; j < piles[i].length && j < k; j++) {
            sum+=piles[i][j];
            result = Math.max(result, sum + getMaxValue(i + 1, k - j - 1));
        }
        return cache[key] = result;
    }
    return getMaxValue(0, k);
};
