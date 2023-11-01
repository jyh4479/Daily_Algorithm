function solution(A, B) {
  let ans = 0;

  const aNumberList = A.slice();
  const bNumberList = B.slice();

  aNumberList.sort((a, b) => Number(a) - Number(b));
  bNumberList.sort((a, b) => Number(b) - Number(a));

  for (let i = 0; i < aNumberList.length; i++) {
    ans += aNumberList[i] * bNumberList[i];
  }

  return ans;
}
