/**
 * @param {number[]} people
 * @param {number} limit
 * @return {number}
 */
var numRescueBoats = function(people, limit) {
    const sortedPeople = people.sort((a,b)=>Number(a)-Number(b)).reverse();
    let ans = 0;

    while(sortedPeople.length>0){
        const head = sortedPeople.shift();
        const tail = sortedPeople.pop();

        if(head + tail > limit) sortedPeople.push(tail);

        ans+=1;
    }

    return ans;
};
