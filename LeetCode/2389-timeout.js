/**
 * @param {number[]} nums
 * @param {number[]} queries
 * @return {number[]}
 */

const solution = (numbers, goal) => {
    let ans = 0;
    const visited = new Array(numbers.length).fill(false);

    const dfs = (start, currentSum, selected, select) => {
        if (selected === select && currentSum <= goal) {
            ans = Math.max(ans, selected);
        } else {
            for (let i = start; i < numbers.length; i++) {
                if (!visited[i]) {
                    visited[i] = true;
                    dfs(i, currentSum + numbers[i], selected + 1, select);
                    visited[i] = false;
                }
            }
        }
    }

    for (let sel = 1; sel <= numbers.length; sel++) {
        dfs(0, 0, 0, sel);
    }

    return ans;
}

var answerQueries = function (nums, queries) {

    const ans = [];

    queries.forEach(goal => {
        ans.push(solution(nums, goal));
    })

    return ans;
};