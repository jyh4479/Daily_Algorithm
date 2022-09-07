function solution(n, words) {
    let answer = [0, 0];
    const usedWord = [];
    let loop = 1;
    let prevWord = "";

    for (let index = 0; index < words.length; index++) {
        const word = words[index];

        if ((index + 1) % n === 1) loop = parseInt((index + 1) / n) + 1;


        //처음 시작
        if (index === 0) {
            usedWord.push(word);
            prevWord = word;
            continue;
        } else {
            //전에 사용한 단어인지 체크, 끝말을 잘 이어갔는지
            if (usedWord.includes(word) || prevWord[prevWord.length - 1] !== word[0]) {
                console.log(word)
                answer = [(index % n) + 1, loop];
                break;
            } else {
                usedWord.push(word);
                prevWord = word;
            }
        }
    }
    return answer;
}