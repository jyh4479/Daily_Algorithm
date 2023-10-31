function solution(s) {

    const numStringList = s.split(" ");
    const numList = numStringList.map(numString => Number(numString));

    numList.sort((a, b) => Number(a) - Number(b));

    let ans = "";

    ans += numList[0];
    ans += ` ${numList[numList.length - 1]}`;

    return ans;
}