/**
 * @param {string} s
 * @return {string[]}
 */
//TODO: 더 좋은 방법 찾기 (이거 너무 어거지)
var restoreIpAddresses = function (s) {

    const ansList = [];

    for (let one = 1; one <= 3; one++) {
        if (s.length < one) break;
        for (let two = 1; two <= 3; two++) {
            if (s.length < (one + two)) break;
            for (let three = 1; three <= 3; three++) {
                if (s.length < (one + two + three)) break;
                for (let four = 1; four <= 3; four++) {
                    if (s.length < (one + two + three + four)) break; else {
                        let curIndex = 0;
                        let ans = "";

                        let slicedString = s.slice(curIndex, one);
                        if (Number(slicedString) > 255 || (slicedString[0] === '0' && slicedString.length > 1)) break;
                        ans += slicedString;
                        ans += '.';
                        curIndex = one;

                        slicedString = s.slice(curIndex, two + curIndex);
                        if (Number(slicedString) > 255 || (slicedString[0] === '0' && slicedString.length > 1)) break;
                        ans += slicedString;
                        ans += '.';
                        curIndex += two;

                        slicedString = s.slice(curIndex, three + curIndex);
                        if (Number(slicedString) > 255 || (slicedString[0] === '0' && slicedString.length > 1)) break;
                        ans += slicedString;
                        ans += '.';
                        curIndex += three;

                        slicedString = s.slice(curIndex, four + curIndex);
                        if (Number(slicedString) > 255 || (slicedString[0] === '0' && slicedString.length > 1)) break;
                        ans += slicedString;

                        if (ans.length === s.length + 3) ansList.push(ans);
                    }
                }
            }
        }
    }

    return ansList;
};