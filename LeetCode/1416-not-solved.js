const mod = 1e9 + 7;
const numberOfArrays = (s, k) => {
    let n = s.length;
    let dp = Array(n + 1).fill(0);
    dp[0] = 1;
    for (let i = 0; i < n; i++) {
        if (s[i] == '0') continue;
        let v = 0;
        for (let j = i; j < n; j++) { // loop all possible values
            v = v * 10 + (s[j] - '0'); // example3: 1 13 131 1317 3 31 317 1 17 7
            if (v >= 1 && v <= k) {
                dp[j + 1] += dp[i];
                dp[j + 1] %= mod;
            } else {
                break;
            }
        }
    }
    return dp[n];
};
