var maxProfit = function(prices) {
    if (!prices || prices.length < 2) return 0; //must buy and sell need at least two days
    let hold = new Array(prices.length).fill(0);
    let nostock = new Array(prices.length).fill(0);
    //init
    hold[0] = -prices[0]; //buy day1
    hold[1] = Math.max(hold[0], -prices[1]); // buy day1 or day2
    nostock[1] = Math.max(0, prices[1] - prices[0]); //sell at least after day1  no benefit or sell day2
    for(let i = 2; i < prices.length; i++){
        hold[i] = Math.max(hold[i-1], nostock[i-2] - prices[i]); //hold i-1  or sell i-2 then can buy now
        nostock[i] = Math.max(nostock[i-1], hold[i-1] + prices[i]); //sell i-1 or hold i-1 still and sell now
    }
    return nostock[prices.length-1]; //only sell all can earn max benefit
};