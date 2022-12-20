/**
 * @param {number[][]} rooms
 * @return {boolean}
 */
var canVisitAllRooms = function (rooms) {
    const visit = new Array(rooms.length).fill(false);

    visit[0] = true;
    let keys = [...rooms[0]];

    while (keys.length > 0) {
        const currentKey = keys.pop();

        if (!visit[currentKey]) {
            visit[currentKey] = true;
            keys = [...keys, ...rooms[currentKey]];
        }
    }

    return visit.includes(false) ? false : true;
};