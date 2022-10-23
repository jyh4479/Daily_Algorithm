const graph = {
    A: ["B", "C"],
    B: ["A", "D"],
    C: ["A", "G", "H", "I"],
    D: ["B", "E", "F"],
    E: ["D"],
    F: ["D"],
    G: ["C"],
    H: ["C"],
    I: ["C", "J"],
    J: ["I"]
};

// queue를 이용한 dfs, bfs
/*

원래 stack, queue를 각각 이용해 dfs, bfs를 구현하지만
js에서는 구조 분해 할당을 통해 자료구조 한가지를 통해 모두 구현할 수 있다.

 */
const dfs = (start) => {
    const visited = [];
    let needVisit = [];

    needVisit.push(start);

    while (needVisit.length > 0) {
        const node = needVisit.shift();

        if (!visited.includes(node)) {
            visited.push(node);

            //구조분해 할당이 일어나는 부분
            needVisit = [...graph[node], ...needVisit];

        }
    }

    return visited;
}

console.log(dfs("A"));