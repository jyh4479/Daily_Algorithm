const getLCM = (a, b) => {
  let count = 1;
  let ans = a;

  while (ans < a * b) {
    if (ans % a === 0 && ans % b === 0) return ans;

    count++;
    ans = a * count;
  }

  return ans;
};

function solution(arr) {
  const numList = arr.slice().sort((a, b) => a - b);
  let currentResult = numList[0];

  for (let i = 1; i < numList.length; i++) {
    currentResult = getLCM(Math.min(numList[i], currentResult), Math.max(numList[i], currentResult));
  }

  return currentResult;
}
