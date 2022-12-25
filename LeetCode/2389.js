// /**
//  * @param {number[]} nums
//  * @param {number[]} queries
//  * @return {number[]}
//  */

// const solution = (numbers,goal) => {
//     let ans = 0;
//     const visited = new Array(numbers.length).fill(false);

//     const dfs = (start, currentSum, selected, select) => {
//         if(selected === select && currentSum<=goal){
//             ans=Math.max(ans,selected);
//         } else {
//             for(let i=start;i<numbers.length;i++){
//                 if(!visited[i]){
//                     visited[i]=true;
//                     dfs(i,currentSum+numbers[i],selected+1,select);
//                     visited[i]=false;
//                 }
//             }
//         }
//     }

//     for(let sel = 1;sel<=numbers.length;sel++){
//         dfs(0,0,0,sel);
//     }

//     return ans;
// }

// var answerQueries = function(nums, queries) {

//     const ans = [];

//     queries.forEach(goal => {
//         ans.push(solution(nums,goal));
//     })

//     return ans;
// };

const getMaxNumbers = (numbers, goal) => {
    let sum = numbers.reduce((a, b) => a + b, 0);
    let ans = numbers.length;

    for (let i = 0; i < numbers.length; i++) {
        // console.log(sum,numbers[i], goal, ans)
        if (sum <= goal) return ans;
        else {
            sum -= numbers[i];
            ans -= 1;
        }
    }

    return 0;
}

var answerQueries = function (nums, queries) {
    const numbers = nums.map(data => Number(data));

    //number에 대한 array sorting 함수 꼭 함수 사용해야하나?
    numbers.sort((a, b) => b - a);

    const ans = [];
    queries.forEach(data => {
        ans.push(getMaxNumbers(numbers, data));
    })

    return ans;
};