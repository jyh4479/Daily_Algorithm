function solution(n) {
  const numList = new Array(2001).fill(0);

  numList[1] = 1;
  numList[2] = 2;

  for (let i = 3; i < numList.length; i++) {
    numList[i] = (numList[i - 1] + numList[i - 2]) % 1234567;
  }

  return numList[n];
}
