const max = Math.max;
const min = Math.min;
const mincostTickets = (days, costs) => {
    let n = days.length;
    let dp = new Array(366).fill(Number.MAX_VALUE);
    for (const day of days) {
        dp[day] = 0;
    }
    dp[0] = 0;
    for (let i = 1; i <= days[n - 1]; i++) {
        if (dp[i] == Number.MAX_VALUE) {
            dp[i] = dp[i - 1];
        } else {
            dp[i] = min(dp[i - 1] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2]);
        }
    }
    return dp[days[n - 1]];
};
