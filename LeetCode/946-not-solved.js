
/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
var validateStackSequences = function(pushed, popped) {
    if (pushed.length === 0 && popped.length === 0 ) {
        return true;
    }
    
    if (pushed.length !== popped.length) {
        return false;
    }

    let stack = [];
    stack.push(pushed.shift());
    
    for (let i = 0; i < popped.length; i++) {
        const poppedNum = popped[i];

        if (poppedNum === stack[stack.length - 1]) {
            stack.pop();
        } else {
            if (pushed.length < 1) {
                return false;
            }

            let found = false;

            while(pushed.length) {
                const num = pushed.shift();
                
                if (num !== poppedNum) {
                    stack.push(num)
                } else {
                    found = true;
                    break;
                }
            }

            if (!found) {
                return false;
            }
        }
    }
    
    return stack.length < 1;
};
