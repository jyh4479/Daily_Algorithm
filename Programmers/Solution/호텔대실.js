function solution(book_time) {
    let ans = 0;
    let usingRoomList = [];

    const timeList = book_time.map(bookTime => {
        const [startHour, startMin] = bookTime[0].split(':');
        const [endHour, endMin] = bookTime[1].split(':');

        return [Number(startHour) * 60 + Number(startMin), Number(endHour) * 60 + Number(endMin) + 10];
    })

    for (let currentTime = 0; currentTime <= 1440; currentTime++) {
        //사용 끝난 방
        usingRoomList = usingRoomList.filter(time => time[1] !== currentTime);

        //사용 시작하는 방
        for (let k = 0; k < timeList.length; k++) {
            if (currentTime === timeList[k][0]) usingRoomList.push(timeList[k]);
        }

        ans = Math.max(ans, usingRoomList.length);
    }

    return ans;
}