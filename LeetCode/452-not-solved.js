/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function (points) {
    points.sort((i1, i2) => {
        if (i1[0] !== i2[0]) {
            return i1[0] - i2[0];
        } else {
            return i1[1] - i2[1];
        }
    });

    let prevInterval = null, count = 0;
    for (const p of points) {
        if (!prevInterval) {
            prevInterval = p;
            count++;
            continue;
        }

        if ((prevInterval[1] <= p[1] && prevInterval[1] >= p[0]) || (p[1] <= prevInterval[1] && p[1] >= prevInterval[0])) {
            prevInterval[0] = Math.max(prevInterval[0], p[0]);
            prevInterval[1] = Math.min(prevInterval[1], p[1]);
        } else {
            prevInterval = p;
            count++;
        }
    }

    return count;
};