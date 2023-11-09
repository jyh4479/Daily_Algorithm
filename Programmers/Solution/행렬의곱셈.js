function solution(arr1, arr2) {
  const ans = [];

  const n = arr1.length;
  const m = arr2[0].length;

  const firstArray = arr1.slice();
  const secondArray = [];

  for (let i = 0; i < arr2[0].length; i++) {
    const subArray = [];
    for (let j = 0; j < arr2.length; j++) {
      subArray.push(arr2[j][i]);
    }
    secondArray.push(subArray);
  }

  for (let i = 0; i < n; i++) {
    const subArray = [];
    for (let j = 0; j < m; j++) {
      const sum = firstArray[i].map((value, index) => value * secondArray[j][index]).reduce((a, b) => a + b, 0);

      subArray.push(sum);
    }
    ans.push(subArray);
  }

  return ans;
}
