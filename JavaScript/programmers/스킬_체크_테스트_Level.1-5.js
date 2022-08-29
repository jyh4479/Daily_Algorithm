function solution(numbers) {

    let numberObj = {0: false, 1: false, 2: false, 3: false, 4: false, 5: false, 6: false, 7: false, 8: false, 9: false}

    numbers.forEach(data => {
        numberObj[Number(data)] = true;
    })

    let answer = 0;

    for (let key in numberObj) {
        if (!numberObj[key]) {
            answer += Number(key);
        }
    }

    return answer;
}