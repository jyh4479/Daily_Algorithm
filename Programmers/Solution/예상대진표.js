const getSqrtNumber = (number) => {
    let ans = 0;
    let num = number;

    while (num > 1) {
        ans++;
        num /= 2;
    }

    return ans;
}

function solution(n, a, b) {
    let start = 1;
    let end = n;
    let center = parseInt((1 + n) / 2);
    let ans = getSqrtNumber(n);

    while (center > 0) {
        if (a <= center && b <= center) {
            end = center;
            center = parseInt((start + end) / 2);
        } else if (a > center && b > center) {
            start = center;
            center = parseInt((start + end) / 2);
        } else {
            return ans;
        }
        ans--;
    }

    return ans;
}