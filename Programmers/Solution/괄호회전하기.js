const checkCorrect = (markString) => {
  const stack = [];

  for (let i = 0; i < markString.length; i++) {
    const currentString = markString[i];
    const currentLastString = stack[stack.length - 1];

    if (stack.length === 0) stack.push(currentString);
    else {
      if (currentString === "]" && currentLastString === "[") stack.pop();
      else if (currentString === "}" && currentLastString === "{") stack.pop();
      else if (currentString === ")" && currentLastString === "(") stack.pop();
      else stack.push(currentString);
    }
  }

  return stack.length > 0 ? false : true;
};

function solution(s) {
  let ans = 0;

  for (let i = 0; i < s.length; i++) {
    const rotateStrin = s.slice(i, s.length) + s.slice(0, i);
    checkCorrect(rotateStrin) ? ans++ : ans;
  }

  return ans;
}
