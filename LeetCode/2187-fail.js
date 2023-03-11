// /**
//  * @param {number[]} time
//  * @param {number} totalTrips
//  * @return {number}
//  */
// const findMinTime = (reverseTime, currentTime, currentTripCount, targetTripCount) => {
//     let curTime = 0;
//     let curTripCount = currentTripCount;
//     const visit = reverseTime.map(t=>false);

//     while(curTripCount>=targetTripCount){
//         reverseTime.forEach((time, index)=>{
//             if((currentTime-curTime) % time === 0) curTripCount-=1;
//         })
//         curTime+=1;
//     }

//     return (currentTime-curTime)+1;
// }

// var minimumTime = function(time, totalTrips) {
//     const maxTime = Math.max(...time);
//     const tripCount = time.map(t=>parseInt(maxTime/t)).reduce((a,b)=>a+b,0);

//     let result = 0;
//     let checkTripCount = 0;

//     while(checkTripCount<totalTrips) {
//         result+=maxTime;
//         checkTripCount+=tripCount;
//     }

//     return findMinTime(time, result, checkTripCount, totalTrips);
// };

/**
 * @param {number[]} time
 * @param {number} totalTrips
 * @return {number}
 */
var minimumTime = function(time, totalTrips) {
    let l = 0;
    let min = Number.MAX_SAFE_INTEGER;
    for (let t of time) {
        min = Math.min(min, t);
    }
    let r = min* totalTrips+1;
    while (l+1 < r){
        let mid = Math.floor((l+r)/2);
        let currTrip = getTrips(mid);
        if (currTrip < totalTrips) {
            l = mid;
        } else {
            r = mid;
        }
    }
    function getTrips(num) {
        let trip = 0;
        for (let t of time) {
            trip+= Math.floor(num/ t);
        }
        return trip;
    }
    return r;
};
