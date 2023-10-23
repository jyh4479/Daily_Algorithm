function solution(input_string) {
    const answer = [];
    const stringObj = {};
    const countObj = {};

    const inputString = input_string.slice();

    for (let i = 0; i < inputString.length; i++) {
        if (stringObj[inputString[i]] === undefined) stringObj[inputString[i]] = 1;
        else stringObj[inputString[i]]++;
    }

    for (const key in stringObj) {
        countObj[key] = 0;
    }

    let prev = 0;
    countObj[inputString[prev]]++;
    for (let cur = 1; cur < inputString.length; cur++, prev++) {
        if (inputString[prev] !== inputString[cur]) {
            countObj[inputString[cur]]++;
        }
    }

    for (let key in stringObj) {
        if (stringObj[key] >= 2 && countObj[key] >= 2) {
            answer.push(key);
        }
    }

    answer.sort();

    return answer.length > 0 ? answer.join("") : "N";
}