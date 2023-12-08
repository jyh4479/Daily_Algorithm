function solution(A, B) {
    let ans = 0;

    const numberListA = A.slice();
    const numberListB = B.slice();

    numberListA.sort((a, b) => Number(a) - Number(b));
    numberListB.sort((a, b) => Number(a) - Number(b));

    while (numberListA.length > 0 && numberListB.length > 0) {
        const aNumber = numberListA.pop();
        const bNumber = numberListB.pop();

        if (bNumber > aNumber) {
            ans++;
        } else {
            numberListB.push(bNumber);
            numberListB.shift();
        }
    }

    return ans;
}
