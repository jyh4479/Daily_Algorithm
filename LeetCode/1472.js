/**
 * @param {string} homepage
 */
var BrowserHistory = function(homepage) {
    this.stack = [homepage]
    this.index = 0
};

/** 
 * @param {string} url
 * @return {void}
 */
BrowserHistory.prototype.visit = function(url) {
    this.stack = this.stack.slice(0,this.index+1)
    this.stack.push(url)
    this.index++
};

/** 
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.back = function(steps) {
    if(steps > this.index){
        this.index=0
        return this.stack[this.index]
    }
    this.index -= steps
    return this.stack[this.index]
};

/** 
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.forward = function(steps) {
    if(steps > this.stack.length-1-this.index){
        this.index = this.stack.length-1
        return this.stack[this.stack.length-1]
    }
    this.index += steps
    return this.stack[this.index]
};

/** 
 * Your BrowserHistory object will be instantiated and called as such:
 * var obj = new BrowserHistory(homepage)
 * obj.visit(url)
 * var param_2 = obj.back(steps)
 * var param_3 = obj.forward(steps)
 */
