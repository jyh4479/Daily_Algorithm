/**
 * @param {number[]} salary
 * @return {number}
 */
var average = function(salary) {
    const salaryList = salary.sort((a,b)=>Number(a)-Number(b));

    salaryList.pop();
    salaryList.shift();

    return salaryList.reduce((a,b)=>a+b,0) / salaryList.length;
};
