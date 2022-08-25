function solution(x) {
    const changeNumber = String(x);
    let sum = 0;

    for (let i = 0; i < changeNumber.length; i++) {
        sum += Number(changeNumber[i]);
    }

    return x % sum === 0;
}