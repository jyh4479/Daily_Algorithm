// H-index 문제

function solution(citations) {

    citations.sort();

    let answer = 0;

    for (let i = 0; i < citations.length; i++) {

        if (citations.slice(0, i).length <= citations[i] && citations.slice(i, citations.length).length >= citations[i]) {
            answer = Math.max(answer, citations[i]);
        } else {
            break;
        }
    }

    return answer;
}