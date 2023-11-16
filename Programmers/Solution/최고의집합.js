function solution(n, s) {
  if (s < n) return [-1];

  const numList = [];
  const arraySum = Math.floor(s / n) * n;

  for (let i = 0; i < n; i++) {
    numList.push(Math.floor(s / n));
  }

  let diff = s - arraySum;
  let curIndex = 0;

  while (diff !== 0) {
    if (diff > 0) {
      numList[curIndex % n]++;
      diff--;
    } else {
      numList[curIndex % n]--;
      diff++;
    }
    curIndex++;
  }

  numList.sort();

  return numList;
}
