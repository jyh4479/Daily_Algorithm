const getHeadNumberTail = (fileName) => {
    let [head, number, tail] = ["", "", ""];
    let numberFlag = false;
    let tailFlag = false;
    let numberCount = 0;

    for (let i = 0; i < fileName.length; i++) {
        //isNaN에 공백이 안걸러짐 -> 이부분 답 확인
        if ((Number.isNaN(Number(fileName[i])) || fileName[i] === " ") && !numberFlag) {
            head += fileName[i];
        } else if (!Number.isNaN(Number(fileName[i]))) {
            numberFlag = true;

            if (!tailFlag && numberCount < 5) {
                number += fileName[i];
                numberCount++;
            } else {
                tail += fileName[i];
            }
        } else if (Number.isNaN(Number(fileName[i]))) {
            tailFlag = true;
            tail += fileName[i];
        }
    }

    return [head, number, tail];
}

const fileSort = (a, b) => {

    const [aHead, aNumber, aTail] = getHeadNumberTail(a);
    const [bHead, bNumber, bTail] = getHeadNumberTail(b);

    if (aHead.toLowerCase() !== bHead.toLowerCase()) {

        const lowerA = aHead.toLowerCase();
        const lowerB = bHead.toLowerCase();

        if (lowerA < lowerB) return -1;
        else if (lowerA > lowerB) return 1;
        return 0

    } else if (Number(aNumber) !== Number(bNumber)) {
        return Number(aNumber) - Number(bNumber);
    }

    return 0;
}

function solution(files) {
    const fileList = files.slice();

    fileList.sort(fileSort);

    return fileList;
}
