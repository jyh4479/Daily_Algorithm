const getNextPos = (y, x, dir) => {
    switch (dir) {
        case 'U':
            return [y - 1, x];
        case 'L':
            return [y, x - 1];
        case 'R':
            return [y, x + 1];
        case 'D':
            return [y + 1, x];
    }
}

function solution(dirs) {
    let ans = 0;

    let curX = 0;
    let curY = 0;

    const visitRecord = {};

    for (let i = 0; i < dirs.length; i++) {
        const [nextY, nextX] = getNextPos(curY, curX, dirs[i]);

        if (nextY < -5 || nextY > 5 || nextX < -5 || nextX > 5) continue;

        if (visitRecord[`from (${curY}, ${curX}) to (${nextY}, ${nextX})`] === undefined &&
            visitRecord[`from (${nextY}, ${nextX}) to (${curY}, ${curX})`] === undefined
        ) {
            visitRecord[`from (${curY}, ${curX}) to (${nextY}, ${nextX})`] = true;
            visitRecord[`from (${nextY}, ${nextX}) to (${curY}, ${curX})`] = true;
            ans++;
        }

        [curY, curX] = [nextY, nextX];
    }

    return ans;
}
