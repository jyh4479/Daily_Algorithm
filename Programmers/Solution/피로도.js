function solution(k, dungeons) {
    let ans = 0;

    const visited = new Array(dungeons.length).fill(false);
    const dl = dungeons.length;

    const numList = [];

    const dfs = (sel, energy) => {

        ans = Math.max(ans, sel);

        for (let i = 0; i < dl; i++) {
            if (!visited[i] && energy >= dungeons[i][0]) {
                visited[i] = true;
                numList.push(i);
                dfs(sel + 1, energy - dungeons[i][1]);
                numList.pop();
                visited[i] = false;
            }
        }
    }

    dfs(0, k);

    return ans;
}
