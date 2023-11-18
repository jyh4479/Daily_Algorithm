const getBinaryCount = (number) => {
    let count = 0;

    for (let i = 0; i < number.length; i++) {
        if (number[i] === '1') count++;
    }

    return count;
}

const getBinaryString = (number) => {
    let binaryNumber = number;
    const result = [];

    while (binaryNumber > 0) {
        result.push(binaryNumber % 2);
        binaryNumber = parseInt(binaryNumber / 2);
    }

    result.reverse();

    return result.join("");
}

function solution(n) {
    const inputCount = getBinaryCount(getBinaryString(n));

    for (let i = n + 1; true; i++) {
        if (inputCount === getBinaryCount(getBinaryString(i))) return i;
    }
}
