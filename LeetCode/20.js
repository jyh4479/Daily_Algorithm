/**
 * @param {string} s
 * @return {boolean}
 */
const checkValid = (a, b) => {
    if(a==='(' && b!==')') return false;
    else if(a==='{' && b!=='}') return false;
    else if(a==="[" && b!==']') return false;
    return true;
}

var isValid = function(s) {
    const checkList = [];

    for(let i=0;i<s.length;i++){
        const check = s[i];

        if(check===')' || check==='}' || check=== ']'){
            const head = checkList.pop();
            if(head===undefined) return false;
            if(!checkValid(head, check)) return false;
        } else {
            checkList.push(check);
        }
    }

    return checkList.length > 0 ? false : true;
};
