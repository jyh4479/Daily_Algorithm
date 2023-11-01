function solution(s) {
    const stringList = s.split(" ");

    let ans = "";

    stringList.forEach(string => {
        ans += `${string.charAt(0).toUpperCase() + string.slice(1).toLowerCase()} `;
    })

    return ans.slice(0, ans.length - 1);
}
