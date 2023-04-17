/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
  const greatCandiesNumber = Math.max(...candies);
  const ans = [];

  candies.forEach(candy=>{
    if(candy+extraCandies>=greatCandiesNumber) ans.push(true);
    else ans.push(false);
  });

  return ans;  
};
