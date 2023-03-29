var maxSatisfaction = function (arr) {
    arr.sort((a, b) => a - b);
    let max = arr.reduce((a, b, i) => a + b * (i + 1));
    let sum = arr.reduce((a, b) => a + b, 0);
    for (let i = 0; i < arr.length; i++) {
        if (max > max - sum)
            return max;
        max -= sum;
        sum -= arr[i];
    }
    return 0;
};