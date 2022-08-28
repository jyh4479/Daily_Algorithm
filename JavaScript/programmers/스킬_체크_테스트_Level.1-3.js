function solution(strings, n) {

    let answer = [];

    const dict = {
        'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [],
        'h': [], 'i': [], 'j': [], 'k': [], 'm': [], 'l': [], 'n': [],
        'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [], 'u': [],
        'v': [], 'w': [], 'x': [], 'y': [], 'z': []
    }

    strings.forEach(string => {
        dict[string[n]].push(string)
    })

    for (let key in dict) {
        dict[key].sort();

        answer.push(...dict[key].map(string => string));
    }

    return answer;
}