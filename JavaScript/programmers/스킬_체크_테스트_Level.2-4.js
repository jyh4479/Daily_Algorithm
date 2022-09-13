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