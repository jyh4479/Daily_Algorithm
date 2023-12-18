function solution(k, dungeons) {
    let ans = 0;

    const visited = new Array(dungeons.length).fill(false);
    const dl = dungeons.length;

    const dfs = (sel, energy) => {

        ans = Math.max(ans, sel);

        for (let i = 0; i < dl; i++) {
            if (!visited[i] && energy >= dungeons[i][0]) {
                visited[i] = true;
                dfs(sel + 1, energy - dungeons[i][1]);
                visited[i] = false;
            }
        }
    }

    dfs(0, k);

    return ans;
}
