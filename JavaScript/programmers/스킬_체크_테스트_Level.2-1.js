function solution(s) {
    let answer = 0;
    const task = [];

    for (let key = 0; key < s.length; key++) {
        task.push(s[key]);
    }

    const check = [];

    task.forEach(data => {
        if (check.length === 0) {
            check.push(data);
        } else {
            if (data === check[check.length - 1]) {
                check.pop();
            } else {
                check.push(data);
            }
        }
    })

    return check.length === 0 ? 1 : 0;
}