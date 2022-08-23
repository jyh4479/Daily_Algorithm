const getCount = (value) => {
    let count = 0;
    for (let i = 1; i <= value; i += 1) {
        if (value % i === 0) {
            count += 1;
        }
    }
    return count;
}

function solution(left, right) {
    let answer = 0;
    for (let cur = left; cur <= right; cur += 1) {
        const checkCount = getCount(cur);
        if (checkCount % 2 === 0) {
            answer += cur;
        } else {
            answer -= cur;
        }
    }
    return answer;
}
