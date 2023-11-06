function solution(elements) {
  const loopNumberList = [...elements, ...elements];
  const N = elements.length;

  const numObject = {};

  for (let i = 1; i <= N; i++) {
    for (let j = 0; j <= loopNumberList.length - i; j++) {
      const sum = loopNumberList.slice(j, j + i).reduce((a, b) => a + b, 0);
      numObject[sum] = true;
    }
  }

  return Object.values(numObject).length;
}
