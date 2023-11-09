function solution(want, number, discount) {
  let ans = 0;

  const wantList = [];
  const totalWantItemCount = number.reduce((a, b) => a + b, 0);

  want.forEach((item, index) => {
    for (let i = 0; i < number[index]; i++) {
      wantList.push(item);
    }
  });

  wantList.sort();

  for (let i = 0; i <= discount.length - totalWantItemCount; i++) {
    const discountList = discount.slice(i, i + totalWantItemCount);
    discountList.sort();

    if (wantList.toString() === discountList.toString()) ans++;
  }

  return ans;
}
