function solution(k, tangerine) {
    let answer = 0;
    let pick = k;

    const tangerObject = {};

    tangerine.forEach(tanger => {
        if (tangerObject[tanger] === undefined) tangerObject[tanger] = 0;
        tangerObject[tanger]++;
    })

    const tangerList = Object.values(tangerObject).sort((a, b) => b - a);

    for (let i = 0; i < tangerList.length; i++) {
        answer++;
        if (tangerList[i] < pick) {
            pick -= tangerList[i];
        } else {
            break;
        }
    }

    return answer;
}