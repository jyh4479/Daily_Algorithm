const getBinaryGap = (binaryString) => {
    const gapList = [];

    let oneCheck = false;
    let currentGap = 0;

    for (let i = 0; i < binaryString.length; i++) {
        const currentChar = binaryString[i];

        if (!oneCheck && currentChar === '1') {
            oneCheck = true;
            continue;
        } else if (oneCheck && currentChar === '1') {
            gapList.push(currentGap);
            currentGap = 0;
            continue;
        } else if (oneCheck && currentChar === '0') {
            currentGap++;
            continue;
        }
    }

    gapList.sort().reverse();

    const ans = gapList[0];

    return ans ?? 0;
}

const getBinaryString = (number) => {
    const binaryList = [];
    let currentNumber = number;

    while (currentNumber > 0) {
        if (currentNumber % 2 === 0) binaryList.push(0);
        else binaryList.push(1);

        currentNumber = parseInt(currentNumber / 2);
    }

    binaryList.reverse();

    return binaryList.join("");
}

const solution = (N) => {
    return getBinaryGap(getBinaryString(N));
}