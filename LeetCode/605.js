/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    const task = flowerbed.map(data=>data);

    if(task.length < 3) {
      if(task.includes(1) && n!==0) return false;
      if(!task.includes(1) && n>1) return false;
      return true;
    } else {
      for(let i=1;i<task.length-1;i++){
        //처음 인덱스에 대한 예외
        if(i===1){
          if(task[i-1] === 0 && task[i] === 0){
            task[i-1]=1;
            n-=1;
          }
        }
        //중간 과정
        if(task[i-1] === 0 && task[i] === 0 && task[i+1] === 0) {
          task[i]=1;
          n-=1;
        }
        //끝 인덱스에 대한 예외
        if(i===task.length-2){
          if(task[i] === 0 && task[i+1] === 0){
            task[i+1]=1;
            n-=1;
          }
        }
        if(n===0) break;
      }
    }
    return n > 0 ? false : true;
};
