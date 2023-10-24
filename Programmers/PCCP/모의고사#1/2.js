// function solution(ability) {
//
//     const ansList = [];
//     const selectedIndex = [];
//
//     const getScore = (personList) => {
//         const selectedSports = [];
//
//         const scoreDfs = (index, sel, score) => {
//             if (sel === personList.length) {
//                 ansList.push(score);
//             } else {
//                 for (let i = 0; i < ability[personList[index]].length; i++) {
//                     if (selectedSports.includes(i)) continue;
//
//                     selectedSports.push(i);
//                     scoreDfs(index + 1, sel + 1, score + ability[personList[index]][i]);
//                     selectedSports.pop();
//                 }
//             }
//         }
//
//         scoreDfs(0, 0, 0);
//     }
//
//     const dfs = (index, sel) => {
//         if (sel === ability[0].length) {
//             getScore(selectedIndex);
//         } else {
//             for (let i = index; i < ability.length; i++) {
//                 selectedIndex.push(i);
//                 dfs(i + 1, sel + 1);
//                 selectedIndex.pop();
//             }
//         }
//     }
//
//     dfs(0, 0);
//
//     ansList.sort((a, b) => Number(b) - Number(a));
//
//     return ansList[0];
// }

function solution(ability) {
    const ansList = [];
    const visited = new Array(ability.length).fill(false);

    const dfs = (sel, sum) => {
        if (sel === ability[0].length) {
            ansList.push(sum);
        } else {
            for (let i = 0; i < ability.length; i++) {
                if (visited[i]) continue;

                visited[i] = true;
                dfs(sel + 1, sum + ability[i][sel]);
                visited[i] = false;
            }
        }
    }

    dfs(0, 0);

    ansList.sort((a, b) => Number(b) - Number(a));

    return ansList[0];
}