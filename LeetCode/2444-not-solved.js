const countSubarrays = (a, L, R) => {
    let n = a.length, l = -1, rmin = -1, rmax = -1, res = 0;
    for (let i = 0; i < n; i++) {
        if (a[i] < L || a[i] > R) l = i;
        if (a[i] == L) rmin = i;
        if (a[i] == R) rmax = i;
        let cnt = Math.min(rmin, rmax) - l;
        res += Math.max(0, cnt);
    }
    return res;
};
