function solution(X, Y) {
    var answer = '';

    const numberObj = {};
    const commonNumber = [];

    for (let i = 0; i < X.length; i++) {
        if (numberObj[X[i]] === undefined) {
            numberObj[X[i]] = 1;
        } else {
            numberObj[X[i]]++;
        }
    }

    for (let i = 0; i < Y.length; i++) {
        //공통 숫자존재하는 경우
        if (numberObj[Y[i]] > 0 && numberObj[Y[i]] !== undefined) {
            commonNumber.push(Y[i]);
            numberObj[Y[i]]--;
        }
    }

    commonNumber.sort().reverse();

    let result = commonNumber.join("");

    if (result === "") result = '-1';
    else if (result[0] === '0') result = '0';

    return result;
}