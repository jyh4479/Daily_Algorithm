/**
 * @param {number[][]} tasks
 * @return {number[]}
 */
var getOrder = function (tasks) {
    const pq = new MinPriorityQueue({priority: (bid) => bid[1]});

    const TASK_LENGTH = tasks.length;
    let curTime = 0;
    let index = 0;
    let processingTime = 0;
    const ans = [];

    while (tasks.length > 0 || ans.length < TASK_LENGTH) {

        //시간마다 오는 task를 heap에 넣기
        if (tasks.length > 0 && tasks[0][0] === curTime) {
            while (tasks.length > 0 && tasks[0][0] === curTime) {
                //다음 할일에 대한 목록
                pq.enqueue([...tasks.shift(), index]);
                index++;
            }
        }

        //스레드가 일하는중인지 판단
        if (processingTime <= 0 && pq.size() > 0) {
            const task = pq.dequeue().element;
            processingTime = task[1];
            ans.push(task[2]);
        }

        processingTime--;
        curTime++;
    }

    return ans;
};