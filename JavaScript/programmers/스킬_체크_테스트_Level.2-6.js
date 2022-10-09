function solution(s) {

    let minNumber = Number.MAX_VALUE;
    //MIN_VALUE는 양수중에서 가장 작은수
    let maxNumber = Number.NEGATIVE_INFINITY;

    const numberList = s.split(' ');
    numberList.forEach(data => {
        minNumber = Math.min(minNumber, Number(data));
        maxNumber = Math.max(maxNumber, Number(data));
    })

    return `${minNumber} ${maxNumber}`;
}