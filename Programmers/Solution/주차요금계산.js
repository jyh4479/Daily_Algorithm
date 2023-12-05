const getMinute = (time) => {
    const [hour, min] = time.split(":");

    return Number(hour) * 60 + Number(min);
}

function solution(fees, records) {
    const answer = [];
    const carParkingInfo = {};
    const carParkingTime = {};

    records.forEach(record => {
        const [time, carNumber, status] = record.split(" ");
        const minute = getMinute(time);

        if (carParkingTime[carNumber] === undefined) {
            carParkingTime[carNumber] = 0;
        }

        if (carParkingInfo[carNumber] === undefined) {
            carParkingInfo[carNumber] = minute;
        } else {
            carParkingTime[carNumber] += minute - carParkingInfo[carNumber];
            delete carParkingInfo[carNumber];
        }
    })

    for (let carNumber in carParkingInfo) {
        carParkingTime[carNumber] += getMinute("23:59") - carParkingInfo[carNumber]
    }

    const carNumberList = Object.keys(carParkingTime);
    carNumberList.sort();

    const [baseTime, baseFee, unitTime, unitFee] = fees;

    carNumberList.forEach(carNumber => {
        const overTime = carParkingTime[carNumber] - baseTime;

        if (overTime > 0) {
            let fee = baseFee + parseInt(overTime / unitTime) * unitFee;
            overTime % unitTime !== 0 ? fee += unitFee : fee;
            answer.push(fee);
        } else {
            answer.push(baseFee);
        }
    })

    return answer
}
