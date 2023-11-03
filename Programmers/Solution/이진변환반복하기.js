const getNewBinaryString = (n) => {
    let binaryList = [];
    let number = n;

    while (number > 0) {
        binaryList.push(number % 2);
        number = parseInt(number / 2);
    }

    return binaryList.reverse().join("");
}

const getTransformBinaryString = (binaryString) => {
    return binaryString.split('0').length - 1;
}

function solution(s) {

    let binaryString = s.slice();
    let binaryTransformCount = 0;
    let zeroCount = 0;

    while (binaryString !== '1') {
        binaryTransformCount++;

        const currentZeroCount = getTransformBinaryString(binaryString);
        zeroCount += currentZeroCount;
        binaryString = getNewBinaryString(binaryString.length - currentZeroCount);
    }

    return [binaryTransformCount, zeroCount];
}