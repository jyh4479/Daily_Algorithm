// function solution(s) {
//
//     const q = [];
//
//     for (let i = 0; i < s.length; i++) {
//         if (q.length === 0) {
//             q.unshift(s[i]);
//         } else {
//             if (s[i] === ')' && q[0] === '(') {
//                 q.shift();
//             } else {
//                 q.unshift(s[i]);
//             }
//         }
//     }
//
//     return q.length <= 0;
// }

// shift, unshift 성능이 안좋음

function solution(s) {

    const q = [];

    for (let i = 0; i < s.length; i++) {
        if (q.length === 0) {
            q.push(s[i]);
        } else {
            if (s[i] === ')' && q[0] === '(') {
                q.pop();
            } else {
                q.push(s[i]);
            }
        }
    }

    return q.length <= 0;
}

// 최근 풀이 --> 
// function solution(s) {
//     const checkArray = [];

//     for (let i = 0; i < s.length; i++) {
//         const mark = s[i];
//         if (checkArray.length === 0) {
//             checkArray.push(mark);
//         } else {
//             if (mark === ')') {
//                 if (checkArray[checkArray.length - 1] === '(') {
//                     checkArray.pop();
//                 } else {
//                     checkArray.push(mark);
//                 }
//             } else if (mark === '(') {
//                 checkArray.push(mark);
//             }
//         }
//     }

//     return checkArray.length === 0;
// }
