/**
 * @param {string} homepage
 */
var BrowserHistory = function(homepage) {
  this.history = [homepage];
  this.forwardHistory = [];
  return null;
};

/** 
 * @param {string} url
 * @return {void}
 */
BrowserHistory.prototype.visit = function(url) {
  this.history.push(url);
  this.forwardHistory = [];
  return null;
};

/** 
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.back = function(steps) {
  while(steps>0 && this.history.length > 1){
    steps-=1;
    this.forwardHistory.push(this.history.pop());
  }
  return this.history[this.history.length-1];
};

/** 
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.forward = function(steps) {
  while(steps>0){
    steps-=1;
    const forward = this.forwardHistory.pop();
    if(forward===undefined) break;
    this.history.push(forward);
  }
  return this.history[this.history.length-1];
};

/** 
 * Your BrowserHistory object will be instantiated and called as such:
 * var obj = new BrowserHistory(homepage)
 * obj.visit(url)
 * var param_2 = obj.back(steps)
 * var param_3 = obj.forward(steps)
 */
