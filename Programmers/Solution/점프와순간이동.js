function solution(n) {
    let currentPoint = n;
    let ans = 0;

    while (currentPoint > 0) {
        if (currentPoint % 2 === 1) {
            currentPoint--;
            ans++;
        } else {
            currentPoint /= 2;
        }

    }

    return ans;
}