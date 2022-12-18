/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    let nums = [];
    let operators = new Set();
    operators.add("+");
    operators.add("-");
    operators.add("*");
    operators.add("/");
    for (let t of tokens) {
        if (operators.has(t)) {
            let value2 = nums.pop();
            let value1 = nums.pop();
            if (t === '+') {
                nums.push(value1 + value2);
            } else if (t === '-') {
                nums.push(value1 - value2);
            } else if (t === '*') {
                nums.push(value1 * value2);
            } else {
                let v = value1/ value2;
                if (v < 0) {
                    v = Math.ceil(v);
                } else {
                    v = Math.floor(v);
                }
                nums.push(Math.floor(v));
            }
        } else {
            nums.push(parseInt(t));
        }
    }
    return nums.pop();
};