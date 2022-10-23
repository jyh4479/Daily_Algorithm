function solution(maps) {
    const direction = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    const maxY = maps.length - 1;
    const maxX = maps[0].length - 1;
    let q = [];

    //시작
    let result = -1;
    q.push([0, 0]);

    while (q.length > 0) {
        // const now = q.shift();
        const now = q.pop();
        const y = now[0];
        const x = now[1];

        if (maxY === y && maxX === x) {
            result = maps[y][x];
            break;
        }

        for (let i = 0; i < 4; i++) {

            const dy = y + direction[i][0];
            const dx = x + direction[i][1];

            if (dy < 0 || dx < 0 || dy > maxY || dx > maxX) continue;
            else {
                //갈수 있는 길인지 판단
                //1이 아니면 이미 방문한것으로 판단
                if (maps[dy][dx] === 1) {
                    maps[dy][dx] = maps[y][x] + 1;
                    // q.push([dy,dx]);
                    q = [[dy, dx], ...q];
                }
            }
        }
    }

    return result;
}

/*

shift 사용은 성능 저하 발생함
pop, 구조분해할당으로 문제 해결

*/