/**
 * @param {number[]} tasks
 * @return {number}
 */
var minimumRounds = function (tasks) {
    const taskObject = {};

    tasks.forEach(task => {
        if (taskObject[task] === undefined) taskObject[task] = 1;
        else taskObject[task]++;
    })

    let ans = 0;

    //1. 3으로 먼저 나눠지는지 확인 (되면 3, 안되면 2 빼기로 반복)
    for (let key in taskObject) {
        let taskAmount = taskObject[key];
        while (taskAmount > 0) {
            if (taskAmount <= 1) return -1;
            if (taskAmount % 3 === 0) {
                taskAmount -= 3;
                ans++;
            } else {
                taskAmount -= 2;
                ans++;
            }
        }
    }

    return ans;
};